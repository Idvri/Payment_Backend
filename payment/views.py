import stripe

from django.http import JsonResponse
from django.shortcuts import render

from stripe.checkout import Session

from config.settings import STRIPE_SK, STRIPE_PK

from payment.models import Item

stripe.api_key = STRIPE_SK


# Create your views here.

def session_view(request, pk):
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


def item_view(request, pk):
    item = Item.objects.filter(pk=pk).first()
    return render(request, 'payment/item_view.html', context={'item': item, 'stripe_pk': STRIPE_PK})
