import stripe
from rest_framework.response import Response

from rest_framework.views import APIView

from stripe.checkout import Session

from payment.models import Item

stripe.api_key = 'sk_test_51NxDJqDLwcpdlOQT8uwljcHQdCpR92rSjQvt0GKExTcNKMVspaX1JLQnxsHoJwfDA7so3EZ0SrerYWJXGRJJSMu800E3Iyl7I4'


# Create your views here.
class BuyAPIView(APIView):

    def get(self, request, pk):
        item = Item.objects.filter(id=pk).first()
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
        return Response({'session_id': session.id})
