import stripe
from stripe import InvalidRequestError

from stripe.checkout import Session

from django.http import JsonResponse
from django.shortcuts import render

from config.settings import STRIPE_SK, STRIPE_PK

from payment.models import Item, Order

stripe.api_key = STRIPE_SK


# Create your views here.

def buy_view(request, pk):
    item = Item.objects.filter(pk=pk).first()
    session = Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price
            },
            'quantity': 1
        }],
        mode="payment",
        success_url='https://example.com/success'
    )
    return JsonResponse({'id': session.id})


def buy_order_view(request, pk):
    order = Order.objects.filter(pk=pk).first()
    price_amount = sum([item.price for item in order.items.all()])
    session = Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': order.name,
                },
                'unit_amount': price_amount
            },
            'quantity': 1
        }],
        mode="payment",
        success_url='https://example.com/success'
    )
    return JsonResponse({'id': session.id})


def item_view(request, pk):
    item = Item.objects.filter(pk=pk).first()
    return render(request, 'payment/item_view.html', context={'item': item, 'stripe_pk': STRIPE_PK})


def order_view(request, pk):
    order = Order.objects.filter(pk=pk).first()
    return render(
        request,
        'payment/order_view.html',
        context={
            'order': order,
            'items': order.items.all(),
            'stripe_pk': STRIPE_PK}
    )
