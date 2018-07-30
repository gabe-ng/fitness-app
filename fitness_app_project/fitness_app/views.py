from django.shortcuts import render, redirect
from .models import User, Custom_Meal, Custom_Circuit
from django.contrib.auth.decorators import login_required
import requests
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User

def landing(request):
    return render(request, 'fitness_app/landing.html', {})

def index(request):
    return render(request, "fitness_app/index.html", {})


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "fitness_app/profile.html", {"username": username})


############## LOG IN ############

# root page
def login_view(request):
    if request.method == "POST":
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    return HttpResponseRedirect("/")
=======
                    return HttpResponseRedirect('/index')
>>>>>>> upstream/master
=======
                    return HttpResponseRedirect('/index')
>>>>>>> upstream/master
=======
                    return HttpResponseRedirect('/index')
>>>>>>> upstream/master
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, "fitness_app/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        # if post, then authenticate (user submitted username and password)
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    return HttpResponseRedirect("/")
=======
                    return redirect('/')
>>>>>>> upstream/master
=======
                    return HttpResponseRedirect('/index')
>>>>>>> upstream/master
=======
                    return HttpResponseRedirect('/index')
>>>>>>> upstream/master
                else:
                    print("The account has been disabled.")
            else:
                HttpResponse(request, "The username and/or password is incorrect.")
    else:
<<<<<<< HEAD
<<<<<<< HEAD
        form = SignupForm()
        return render(request, "fitness_app/signup.html", {"form": form})
=======
        form = LoginForm()
        return render(request, 'fitness_app/login.html', {'form': form})
>>>>>>> upstream/master

=======
        form = LoginForm()
        return render(request, 'fitness_app/signup.html', {'form': form})
>>>>>>> upstream/master


def logout_view(request):
    logout(request)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    return HttpResponseRedirect("/")
=======
    return HttpResponseRedirect('/index')
>>>>>>> upstream/master
=======
    return HttpResponseRedirect('/index')
>>>>>>> upstream/master
=======
    return HttpResponseRedirect('/index')
>>>>>>> upstream/master


############# HOMEPAGE ###########

# homepage


def homepage(request):
    return render(request, "fitness_app/homepage.html")


def food_find(request):
    r = requests.get(
        "https://api.edamam.com/api/food-database/parser?ingr=steak&app_id=2d7d9644&app_key=8e911eeff3b68f04eafd1fffeaf16401",
        params=request.GET,
    )
    return requests.Response


############# PROFILE ###########

# profile


def dashboard(request, username):
    return render(request, "fitness_app/dashboard.html")
