from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.userregister, name='userregister'),
    path('login/', views.userlogin, name='userlogin'),
    path('profile/', views.userprofile, name='userprofile'),
]