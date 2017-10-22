import stripe
import datetime
from django.conf import settings
from celery.decorators import task
from choc_customer.models import Customer
from order.models import Order

stripe.api_key = settings.STRIPE_API_KEY


@task(name='process_order')
def process_order():
    customers = Customer.objects.filter(billing_day=datetime.date.today().day)
    for customer in customers:
        order = Order.objects.get(status='0')
        stripe.Charge.create(
            amount=order.total,
            currency="aud",
            source=customer.stripe_visa_token,
            description="Charge for {0}".format(customer.user.email)
        )
    return

