from django.db import models

class PurchaseRequest(models.Model):
    requester = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class RequestLine(models.Model):
    purchase_request = models.ForeignKey(PurchaseRequest, on_delete=models.CASCADE, related_name='request_lines')
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
