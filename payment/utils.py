from stripe.checkout import Session


def get_session(name, unit_amount):
    return Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': name},
                    'unit_amount': unit_amount,
                },
                'quantity': 1
            }
        ],
        mode="payment",
        success_url='http://localhost:8000/success'
    )
