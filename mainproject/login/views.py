from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from login import config


# # Create your views here.
# def login_def(request):
#     if request.method == 'POST':
#         username = request.POST['loginEmail']
#         password = request.POST['loginPassword']
#         r = login.objects.filter(usnm=username, pswd=password)
#         print(r)
#         if r.count() > 0:
#             return render(request, 'login/home.html')
#         else:
#             return HttpResponse("Unsuccess")
#
#     return render(request, 'login/login.html')


def login_def(request):
    if request.method == 'POST':
        username = request.POST['loginEmail']
        password = request.POST['loginPassword']
        # print(username)
        # print(password)
        user = authenticate(request, username=username, password=password)

        if user.is_superuser:
            return render(request, 'useradmin/adminhome.html')
        elif user:
            login(request, user)
            config.username = str(user.username)
            config.u_id = str(user.id)
            print(type(config.username))

           # print('checking')
            return render(request, 'user/Userbase.html', {'un': username})

        else:
            print('error')
            messages.error(request, 'Invalid credentials !')
            return redirect('login:login')

    else:
        return render(request, 'login/login.html')
# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login:login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'login/user_registration.html', {'form': form})

def signup_view(request):
    form = SignupForm()
    reguserform = RegUserForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        reguserform = RegUserForm(request.POST)

        if form.is_valid()and reguserform.is_valid():
            user = form.save()
            reg = reguserform.save(commit=False)
            reg.user = user
            reg.save()
            return redirect('login:login')
    return render(request, 'login/user_registration.html', {'form': form, 'r_form': reguserform})

def home_page(request):
    return render(request, 'login/home.html')



def test_view(request):

    return render(request, 'login/test.html')


