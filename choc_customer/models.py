from django.db import models
from django.conf import settings
from utils.models import CreateAndUpdateTimeFields
from django.contrib.auth.models import User

# Create your models here.
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)
SUBSCRIPTION_CHOICES = ( ('0', 'Recurrent'), ('1', '6-month'))


class Customer(CreateAndUpdateTimeFields):
    user = models.OneToOneField(USER_MODEL)
    billing_day = models.IntegerField()
    plan = models.CharField(max_length=1, choices=SUBSCRIPTION_CHOICES)
    address = models.TextField()
    stripe_visa_token = models.CharField(max_length=100)

    def __str__(self):
        return "Email: {0}, Plan: {1}".format(self.user.email, self.plan)
