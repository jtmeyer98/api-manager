from rest_framework import serializers
from .models import PurchaseRequest, RequestLine

class RequestLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLine
        fields = ['product', 'quantity', 'price', 'currency', 'purchase_request']

    def validate_purchase_request_id(self, value):
        if not PurchaseRequest.objects.filter(id=value).exists():
            raise serializers.ValidationError("PurchaseRequest con este ID no existe.")
        return value


class PurchaseRequestSerializer(serializers.ModelSerializer):
    request_lines = RequestLineSerializer(many=True, read_only=True)
    class Meta:
        model = PurchaseRequest
        fields = ['id', 'requester', 'description', 'date', 'type', 'status', 'request_lines']