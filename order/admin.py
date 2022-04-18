from django.contrib import admin
from .models import Order


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['ordered_by','mobile','shipping_address', 'subtotal', 'total']
    list_filter = ['ordered_by']
    readonly_fields = ('ordered_by','cart','mobile','shipping_address','subtotal','total','created_at')
    can_delete = False


admin.site.register(Order,OrderAdmin)