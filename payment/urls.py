from django.urls import path

from payment.apps import PaymentConfig
from payment.views import BuyAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('buy/<int:pk>', BuyAPIView.as_view(), name='buy_item'),
]
