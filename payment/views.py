import json

import stripe
from stripe import InvalidRequestError, PaymentIntent

from django.views.decorators.csrf import csrf_exempt


from django.http import JsonResponse
from django.shortcuts import render

from config.settings import STRIPE_SK, STRIPE_PK, CSRF_TRUSTED_ORIGINS

from payment.models import Item, Order
from payment.utils import get_session, validate_items

stripe.api_key = STRIPE_SK


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'payment/index.html')


def buy_view(request, pk):
    if request.method == 'GET':
        item = Item.objects.filter(pk=pk).all()
        if not item:
            return JsonResponse({'detail': 'Nothing here'})
        session = get_session(item)
        return JsonResponse({'id': session.id})


def buy_order_view(request, pk):
    if request.method == 'GET':
        order = Order.objects.filter(pk=pk).first()
        if not order:
            return JsonResponse({'detail': 'Nothing here'})
        elif not order.items.all():
            return JsonResponse({'message': 'Your order is empty'})
        try:
            session = get_session(order.items.all(), order.tax, order.discount)
        except InvalidRequestError as e:
            return JsonResponse({'message': e.user_message})
        else:
            return JsonResponse({'id': session.id})


def item_view(request, pk):
    if request.method == 'GET':
        item = Item.objects.filter(pk=pk).first()
        if not item:
            return render(request, 'payment/nothing_here.html')
        return render(request, 'payment/item_view.html', context={'item': item, 'stripe_pk': STRIPE_PK})


def order_view(request, pk):
    if request.method == 'GET':
        order = Order.objects.filter(pk=pk).first()
        if not order:
            return render(request, 'payment/nothing_here.html')
        return render(
            request,
            'payment/order_view.html',
            context={
                'order': order,
                'items': order.items.all(),
                'stripe_pk': STRIPE_PK,
                'error': validate_items(order.items.all())
            }
        )


def success(request):
    if request.method == 'GET':
        return render(request, 'payment/success_view.html')


def buy_intent_view(request, pk):
    if request.method == 'GET':
        item = Item.objects.filter(pk=pk).first()
        if not item:
            return JsonResponse({'message': 'Nothing here'})
        intent = PaymentIntent.create(
            amount=item.price,
            currency=item.currency,
            payment_method='pm_card_visa',
        )
        return JsonResponse({'detail': intent.id})


@csrf_exempt
def confirm_intent_view(request):
    if request.method == 'POST':
        try:
            intent = PaymentIntent.retrieve(json.loads(request.body)['payment'])
            PaymentIntent.confirm(
                intent.id,
                payment_method=intent.payment_method,
                return_url=f'{CSRF_TRUSTED_ORIGINS[0]}/success',
            )
        except InvalidRequestError as e:
            return JsonResponse({'message': e.user_message})
        else:
            return JsonResponse({'detail': 'Thanks for payment!'})
