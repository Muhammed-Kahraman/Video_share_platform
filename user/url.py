from user import views
from django.urls import path,include
from django.contrib import admin

app_name = "user"

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.loginUser, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),


]