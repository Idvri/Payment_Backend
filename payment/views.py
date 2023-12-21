import stripe

from django.http import JsonResponse
from django.shortcuts import render

from stripe.checkout import Session

from payment.models import Item

stripe.api_key = 'sk_test_51NxDJqDLwcpdlOQT8uwljcHQdCpR92rSjQvt0GKExTcNKMVspaX1JLQnxsHoJwfDA7so3EZ0SrerYWJXGRJJSMu800E3Iyl7I4'


# Create your views here.

def get_session_id(request, pk):
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


def get_item(request, pk):
    item = Item.objects.filter(pk=pk).first()
    return render(request, 'payment/item_view.html', context={'item': item})
