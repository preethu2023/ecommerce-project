
# from . import views
# from django.urls import path
# urlpatterns = [
#     path('customers/', views.customer),
# ]

# urls.py
from django.urls import path
from .views import (
    CustomerListCreateView,
    ProductListCreateView,
    OrderListCreateView,
    OrderUpdateView,
    OrderFilterByProductView,
    OrderFilterByCustomerView,
)

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/filter-by-product/', OrderFilterByProductView.as_view(), name='order-filter-by-product'),
    path('orders/filter-by-customer/', OrderFilterByCustomerView.as_view(), name='order-filter-by-customer'),
]
