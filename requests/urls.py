from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchaseRequestViewSet, RequestLineViewSet

router = DefaultRouter()
router.register(r'purchase_requests', PurchaseRequestViewSet)
router.register(r'request_lines', RequestLineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
