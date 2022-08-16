from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.home, name='home'),
    path("signin",views.signin, name='signin'),
    path("signup",views.signup, name='signup'),
    path("about",views.about,name = "about"),
]
