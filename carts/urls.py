from django.urls import path

from .views import *

app_name = 'carts'

# urlpatterns = [
#     path('', shop_cart, name = 'shop_cart'),
#     path('addtoshopcart/<int:id>', addtoshopcart, name='addtoshopcart'),
#     path('deletefromcart/<int:id>', deletefromcart, name = 'deletefromcart'),
# ]

urlpatterns = [
    path('', MyCartView.as_view(), name = 'shop_cart'),
    path('add-to-cart/<int:pro_id>', AddToCartView.as_view(), name='addtocart'),
    path('deletefromcart/<int:cp_id>/', ManageCartView.as_view(), name = 'deletefromcart'),
    path('empty-cart/', EmptyCartView.as_view(), name = 'emptycart'),
]