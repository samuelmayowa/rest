from django.contrib import admin
from carts.models import Cart, CartProduct


@admin.register(Cart)
class MealAdmin(admin.ModelAdmin):
    list_display = ['user', 'total']
    list_filter = ['created_at']

@admin.register(CartProduct)
class MealAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product','rate', 'quantity', 'subtotal']
    list_filter = ['rate', 'product']
