# serializers.py
from rest_framework import serializers
from .models import Indications


class VoltageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indications
        fields = ('time', 'name', 'value')