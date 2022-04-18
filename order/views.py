from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string

from .models import *
from user.models import UserProfile
from carts.models import *
from meals.models import Meals
from django.views.generic import TemplateView, FormView
from .forms import CheckoutForm


class CheckoutView(FormView):
    template_name = "order/order_form.html"
    form_class = CheckoutForm
    success_url = reverse_lazy('meals:meal_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart_obj = Cart.objects.get(id = cart_id)
        else :
            cart_obj = None
        context["cart"] = cart_obj
        return context
    

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            cart_obj = Cart.objects.get(id = cart_id)
            form.instance.cart=cart_obj
            form.instance.subtotal=cart_obj.total
            form.instance.total = cart_obj.total
            form.instance.order_status = 'Order Received'
            messages.success(self.request, 'Thank you for your order')
            del self.request.session['cart_id']
            form.save()
            
        else :
            return redirect('carts:shop_cart')
        return super().form_valid(form)



