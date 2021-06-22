from django.db.models import fields
from rest_framework import serializers
from cars.models import CarsNew

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsNew
        fields = '__all__'

