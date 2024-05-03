from django.urls import path
from .views import HistoricalPerformanceAPIView, VendorListCreateAPIView,PurchaseOrderListCreateAPIView

urlpatterns = [
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('api/HistoricalPerformance/', HistoricalPerformanceAPIView.as_view(), name='Historical-Performance'),
]
