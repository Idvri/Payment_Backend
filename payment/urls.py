from django.urls import path

from payment.apps import PaymentConfig
from payment.views import buy_view, buy_order_view, item_view, order_view, success

app_name = PaymentConfig.name

urlpatterns = [
    path('buy/<int:pk>', buy_view, name='buy'),
    path('buy_order/<int:pk>', buy_order_view, name='buy_order'),
    path('item/<int:pk>', item_view, name='item'),
    path('order/<int:pk>', order_view, name='order'),
    path('success', success, name='success')
]
