from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import Meals
from django.core.paginator import Paginator


# Create your views here.

def meal_list(request):
    meal = Meals.objects.filter(draft=False)
    local_dishes = meal.filter(food_type='local_dishes', special_food=True)[:4]
    fast_food = meal.filter(food_type='fast_food', special_food=True)[:4]
    pizza = meal.filter(food_type='pizza', special_food=True)[:4]
    burger = meal.filter(food_type='burger', special_food=True)[:4]
    soft_drink = meal.filter(food_type='soft_drink', special_food=True)[:4]
    oth = meal.all()[:4]

    # the following handles pagination
    paginator = Paginator(meal, 12)  # shows s-ecifoc number of posts
    page = request.GET.get('page')
    meal = paginator.get_page(page)

    template = 'meals/list.html'

    context = {
        'meals': meal,
        'ld': local_dishes,
        'ff': fast_food,
        'pz': pizza,
        'bg': burger,
        'sd': soft_drink,
        'all': oth,
    }

    return render(request, template, context)


def meal_details(request, slug):
    meal_detail = get_object_or_404(Meals, slug=slug)
    meal_slide = meal_detail.meals.all()
    meal = Meals.objects.filter(draft=False)
    template = 'meals/details.html'
    context = {
        'details': meal_detail,
        'meal_slide': meal_slide,
        'meal': meal,
    }

    return render(request, template, context)


class SearchListView(ListView):
    model = Meals
    template_name = "meals/list.html"

    def get_query_set(self):
        # this is for meal search
        search_query = self.request.GET.get('q')
        if search_query:
            meal = self.model.objects.filter(
                Q(name__icontains=search_query) | Q(
                    description__icontains=search_query)
                | Q(food_type__icontains=search_query) | Q(price__icontains=search_query)
            ).distinct()
        else:
            meal = self.model.objects.none()
        return meal
