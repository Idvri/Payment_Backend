from stripe import TaxRate, Coupon
from stripe.checkout import Session

from config.settings import CSRF_TRUSTED_ORIGINS
from payment.models import Tax, Discount


def get_session(name, unit_amount, tax_rate: Tax = None, discount: Discount = None):
    return Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': name},
                    'unit_amount': int(unit_amount * 100),
                },
                'quantity': 1,
                'tax_rates': get_tax(tax_rate),
            }
        ],
        discounts=[{'coupon': get_discount(discount)}],
        mode="payment",
        success_url=f'{CSRF_TRUSTED_ORIGINS[0]}/success'
    )


def get_tax(tax: Tax = None):
    if tax is None:
        return None
    return [TaxRate.create(
        display_name="Налог",
        inclusive=True,
        percentage=tax.value,
    ).id]


def get_discount(discount: Discount = None):
    if discount is None:
        return None
    return Coupon.create(
        percent_off=discount.value,
        duration="once",
    )
