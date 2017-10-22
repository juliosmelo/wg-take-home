from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from utils.models import CreateAndUpdateTimeFields
from choc_customer.models import Customer
# Create your models here.

ORDER_STATUS_CHOICES = (
    ('0', 'Open'),
    ('1, 'Closed'),
)

class Order(CreateAndUpdateTimeFields):
    customer = models.ForeignKeyField('Customer', related_name='orders', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES)
    stripe_token = models.CharField(max_length=100)
    def __str__(self):
        return self.customer.user.email


class OrderItem(CreateAndUpdateTimeFields):
    order = models.ForeignKeyField('Order', related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKeyField(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag
