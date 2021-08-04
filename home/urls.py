from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('ind/',views.index,name='ind')
] 