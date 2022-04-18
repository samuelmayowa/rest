from user.models import UserProfile
from django.db import models
from django.forms import ModelForm
from meals.models import Meals


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Cart: '+ str(self.id) 
    

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Meals, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Cart: '+ str(self.cart.id) + 'Cart Product: '+ str(self.product.name) 
      