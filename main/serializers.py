from rest_framework import serializers
from .models import Deals


class DealsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(DealsSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Deals
        fields = ['customer', 'item', 'total', 'quantity', 'date']
