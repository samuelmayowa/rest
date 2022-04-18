from django.shortcuts import render, redirect, get_object_or_404
from meals.models import Meals, WhyChooseUs, Contact_us, Testimonials, About_us, Message
from .forms import MessageForm
from django.contrib import messages


def home(request):
    food = Meals.objects.all()
    local_dishes = food.filter(food_type='local_dishes')[:12]
    fast_food = food.filter(food_type='fast_food')[:12]
    pizza = food.filter(food_type='pizza')[:12]
    burger = food.filter(food_type='burger')[:12]
    soft_drink = food.filter(food_type='soft_drink')[:12]
    oth = food.all()[:12]

    testimony = Testimonials.objects.all()
    # below is forced to show only one content in the front page
    why_choose_us = WhyChooseUs.objects.all()[:1]
    banner = food.filter(banner=True)[:1]

    context = {
        'ld': local_dishes,
        'ff': fast_food,
        'pz': pizza,
        'bg': burger,
        'sd': soft_drink,
        'all': oth,
        'testimony': testimony,
        'why_choose_us': why_choose_us,
        'banner': banner,
    }

    template = 'home.html'
    return render(request, template, context)


def about(request):
    testimonials = Testimonials.objects.all()
    about_us = get_object_or_404(About_us)
    context = {
        'about': about_us,
        'testimonials': testimonials
    }
    template = 'about.html'
    return render(request, template, context)


def footer(request):
    contact_us = get_object_or_404(Contact_us)
    meal = Meals.objects.all()
    hot_menu = meal.filter(hot_menu=True)[:6]
    template = 'footer.html'
    context = {
        'contact': contact_us,
        'hot_menu': hot_menu,
    }
    return render(request, template, context)


def cart(request):
    template = 'meals/cart.html'
    return render(request, template)


def contact(request):
    contact_us = get_object_or_404(Contact_us)
    if request.method == 'POST':
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form.save(commit=True)
            # redirect with the success message
            messages.success(request, 'Message sent successfully',
                             extra_tags='success')
            return redirect(to='contact_us')
        else:
            messages.error(request, 'An unexpected error has occured.',
                           extra_tags='error')

    form = MessageForm()
    template = 'contact.html'
    context = {
        'message': form,
        'contact': contact_us,
    }

    return render(request, template, context)