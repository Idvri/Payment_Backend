import stripe

from django.http import JsonResponse
from django.shortcuts import render

from config.settings import STRIPE_SK, STRIPE_PK

from payment.models import Item, Order
from payment.utils import get_session

stripe.api_key = STRIPE_SK


# Create your views here.
def index(request):
    return render(request, 'payment/index.html')


def buy_view(request, pk):
    item = Item.objects.filter(pk=pk).first()
    if not item:
        return JsonResponse({'detail': 'nothing here'})
    session = get_session(item.name, item.price)
    return JsonResponse({'id': session.id})


def buy_order_view(request, pk):
    order = Order.objects.filter(pk=pk).first()
    if not order:
        return JsonResponse({'detail': 'nothing here'})
    price_amount = sum([item.price for item in order.items.all()])
    session = get_session(order.name, price_amount)
    return JsonResponse({'id': session.id})


def item_view(request, pk):
    item = Item.objects.filter(pk=pk).first()
    if not item:
        return render(request, 'payment/nothing_here.html')
    return render(request, 'payment/item_view.html', context={'item': item, 'stripe_pk': STRIPE_PK})


def order_view(request, pk):
    order = Order.objects.filter(pk=pk).first()
    if not order:
        return render(request, 'payment/nothing_here.html')
    return render(
        request,
        'payment/order_view.html',
        context={
            'order': order,
            'items': order.items.all(),
            'stripe_pk': STRIPE_PK
        }
    )


def success(request):
    return render(request, 'payment/success_view.html')
