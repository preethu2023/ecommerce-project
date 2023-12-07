from django.shortcuts import render, HttpResponse

# # Create your views here.
# def customer(request):
#     # Your view logic here
#     context = {'name': 'John Doe'}
#     return render(request, 'Shop/home.html', context)

# views.py
from rest_framework import generics
from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderFilterByProductView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        products = self.request.query_params.get('products', '').split(',')
        return Order.objects.filter(order_item__product__name__in=products).distinct()

class OrderFilterByCustomerView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        customer_name = self.request.query_params.get('customer', '')
        return Order.objects.filter(customer__name=customer_name)



