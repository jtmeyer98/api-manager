from rest_framework import serializers
from .models import PurchaseRequest, RequestLine

class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = '__all__'

class RequestLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLine
        fields = '__all__'
