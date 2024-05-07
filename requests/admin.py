from django.contrib import admin
from .models import PurchaseRequest, RequestLine

@admin.register(PurchaseRequest)
class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = ['requester', 'date', 'type', 'status']
    search_fields = ['requester', 'description']
    list_filter = ['status', 'type']

@admin.register(RequestLine)
class RequestLineAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price', 'currency', 'purchase_request']
    search_fields = ['product']
    list_filter = ['currency', 'purchase_request__status'] 
