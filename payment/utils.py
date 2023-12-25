from stripe import TaxRate, Coupon
from stripe.checkout import Session

from config.settings import CSRF_TRUSTED_ORIGINS
from payment.models import Tax, Discount


def get_session(items: list, tax_rate: Tax = None, discount: Discount = None):
    new_items = list()
    for item in items:
        new_items.append({
            'price_data': {
                'currency': item.currency,
                'product_data': {'name': item.name},
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
            'tax_rates': get_tax(tax_rate),
        })
    return Session.create(
        line_items=new_items,
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


def validate_items(items):
    currencies = {item.currency for item in items}
    if len(currencies) > 1:
        return True
    else:
        return False
