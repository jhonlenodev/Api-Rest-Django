from django.db import models
from rest_framework import viewsets
from cars.models import CarsNew
from cars.api.serializers import CarsSerializer

class CarsViewSet(viewsets.ModelViewSet):
    queryset = CarsNew.objects.all()
    serializer_class = CarsSerializer