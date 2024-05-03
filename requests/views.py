from django.shortcuts import render
from rest_framework import viewsets
from .models import PurchaseRequest
from .serializers import PurchaseRequestSerializer

class PurchaseRequestViewSet(viewsets.ModelViewSet):
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer
