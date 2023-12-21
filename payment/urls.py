from django.urls import path

from payment.apps import PaymentConfig
from payment.views import get_session_id, get_item

app_name = PaymentConfig.name

urlpatterns = [
    path('buy/<int:pk>', get_session_id, name='buy_item'),
    path('item/<int:pk>', get_item, name='get_item'),
]
