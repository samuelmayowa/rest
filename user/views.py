from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import SignUpForm
from .models import UserProfile


def user(request):
    return HttpResponse('Works well')


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # the following keeps the user on session so that we can get the image of the user
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            messages.success(request, 'Logged in successful')
            return HttpResponseRedirect('/cart')
        else:
            messages.error(request, 'Invalid Login Details')
            return HttpResponseRedirect('/users/login')
    template = 'user/login.html'
    return render(request, template)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # this makes the possibility of profile creation after login
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'images/users/user.png'
            data.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/users/signup')

    form = SignUpForm()
    template = 'user/signup.html'
    context = {
        'form':form,
    }
    return render(request, template, context)
