
from rest_framework import serializers
from .models import *
class GenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'
