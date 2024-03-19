from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home.html',views.home,name="home.html"),
    path('contact.html',views.contact, name='contact'), 
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
   
]