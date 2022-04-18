from django.urls import path
from .views import user, signup_form, login_form, logout_func

app_name = 'user'
urlpatterns = [
    path('', user, name='user'),
    path('login/', login_form, name='login'),
    path('logout/', logout_func, name='logout_func'),
    path('signup/', signup_form, name='signup'),

]