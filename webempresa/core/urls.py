from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('i7/', views.i7, name="i7"),
]