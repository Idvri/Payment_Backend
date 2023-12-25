from django.urls import path

from payment.apps import PaymentConfig
from payment.views import buy_view, buy_order_view, item_view, order_view, success, index, buy_intent_view, \
    confirm_intent_view

app_name = PaymentConfig.name

urlpatterns = [
    path('', index, name='index'),

    path('buy_intent/<int:pk>', buy_intent_view, name='buy_intent'),
    path('confirm_intent', confirm_intent_view, name='confirm_intent'),

    path('buy/<int:pk>', buy_view, name='buy'),
    path('buy_order/<int:pk>', buy_order_view, name='buy_order'),
    path('item/<int:pk>', item_view, name='item'),
    path('order/<int:pk>', order_view, name='order'),
    path('success', success, name='success')
]
