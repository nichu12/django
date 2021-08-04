from django.contrib.auth import authenticate
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
   path('', views.main,name='main'),
   path('homepage/',views.homepage,name='homepage'),
   path('login/',views.login,name='login'),
   path('register/',views.register,name='reg'),
   path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
  
   
] 