from rest_framework.views import APIView

from stripe.checkout import Session


# Create your views here.
class BuyAPIView(APIView):

    def get(self, pk: int):
        return Session.create()
