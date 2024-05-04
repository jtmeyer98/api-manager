from rest_framework import serializers
from .models import PurchaseRequest, RequestLine

class RequestLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLine
        fields = ['id', 'product', 'quantity', 'price', 'currency']

class PurchaseRequestSerializer(serializers.ModelSerializer):
    request_lines = RequestLineSerializer(many=True, read_only=True)
    class Meta:
        model = PurchaseRequest
        fields = ['id', 'requester', 'description', 'date', 'type', 'status', 'request_lines']