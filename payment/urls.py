from django.urls import path

from payment.apps import PaymentConfig
from payment.views import session_view, item_view

app_name = PaymentConfig.name

urlpatterns = [
    path('buy/<int:pk>', session_view, name='session'),
    path('item/<int:pk>', item_view, name='item'),
]
