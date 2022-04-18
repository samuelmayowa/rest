from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from carts.models import Cart
from phonenumber_field.modelfields import PhoneNumberField

from meals.models import Meals

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=200)
    mobile = PhoneNumberField(max_length=14, region='NG')
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    # payment_method = models.CharField(
    #     max_length=20, choices=METHOD, default="Cash On Delivery")
    # payment_completed = models.BooleanField(
    #     default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)
