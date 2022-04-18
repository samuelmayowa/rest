from django.urls import path

from .views import CheckoutView

app_name = 'orders'

urlpatterns = [
    path('', CheckoutView.as_view(), name = 'order'),
]