from django.shortcuts import render
from rest_framework import viewsets
from .models import PurchaseRequest, RequestLine
from .serializers import PurchaseRequestSerializer, RequestLineSerializer

class PurchaseRequestViewSet(viewsets.ModelViewSet):
    queryset = PurchaseRequest.objects.all().prefetch_related('request_lines')
    serializer_class = PurchaseRequestSerializer

class RequestLineViewSet(viewsets.ModelViewSet):
    queryset = RequestLine.objects.all()
    serializer_class = RequestLineSerializer