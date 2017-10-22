import datetime
from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives
from celery.decorators import task
from choc_customer.models import Customer
from django.conf import settings
from django.template.loader import render_to_string
from stock.models import Chocolate

@task(name='send_recs')
def send_recommendation_mail():
    customers = Customer.objects.filter(billing_day=datetime.date.today().day-2)
    for customer in customers:
        subject, from_email, to = 'Chocolates of month ;)',settings.DEFAULT_FROM_EMAIL, customer.user.email
        email_template_context = {'cholates': Chocolate.get_recommendations(), 'customer': customer}
        text_content = render_to_string('chos_customer/email/rec.txt', email_template_context)
        html_content = render_to_string('chos_customer/email/rec.html', email_template_context)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

