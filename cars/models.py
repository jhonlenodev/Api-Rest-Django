from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from uuid import uuid4

class CarsNew(models.Model):
    id_cars = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    dealership = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to="cars/imagens/%Y/%m/%d", blank=True)
    description = models.TextField()

    def __str__(self):
       return self.name
