from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),  # This should match the 'signin' name in the form action
    path('signout/', views.signout, name="signout"),
]
