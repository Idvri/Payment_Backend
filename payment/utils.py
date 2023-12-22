from stripe.checkout import Session

from config.settings import CSRF_TRUSTED_ORIGINS


def get_session(name, unit_amount):
    return Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': name},
                    'unit_amount': int(unit_amount * 100),
                },
                'quantity': 1
            }
        ],
        mode="payment",
        success_url=f'{CSRF_TRUSTED_ORIGINS[0]}/success'
    )
