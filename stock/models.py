from django.db import models
from utils.models import CreateAndUpdateTimeFields
from .fixtures import dummy_choc
# Create your models here.

CHOC_KIND_CHOICES = (('0', 'dark'), ('1', 'white'))
FRUIT_KIND_CHOICES = (('0', 'fresh'), ('1', 'dry'))


class Product(models.Model):    
    name = models.CharField(max_length=40)
    tags = models.CharField(max_length=255)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    thumb = models.FileField(upload_to='products/uploads/')

    class Meta:
        abstract = True

class Chocolate(CreateAndUpdateTimeFields, Product):
    kind = models.CharField(max_length=1, choices=CHOC_KIND_CHOICES)

    @staticmethod
    def get_recommendations(white_choc=1, dark_choc=1):
        white_data = [d for d in dummy_choc if d['kind'] == 1][:white_choc]
        dark_data = [d for d in dummy_choc if d['kind'] == 0][:dark_choc]
        result = [dict(w,**d) for w in white_data for d in dark_data]
        return result

class Fruit(CreateAndUpdateTimeFields, Product):
    kind = models.CharField(max_length=1, choices=FRUIT_KIND_CHOICES)