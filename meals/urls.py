from django.urls import path
from .views import meal_list, meal_details, SearchListView

app_name = 'meals'

urlpatterns = [
    path('', meal_list, name='meal_list'),
    path('details/<slug:slug>/', meal_details, name='meal_details'),
    path('search/', SearchListView.as_view(), name='search'),
]
