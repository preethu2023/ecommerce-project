
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(25)])

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=255)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

