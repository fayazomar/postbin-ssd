from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Postbin-home'),
    path('about/', views.about, name='Postbin-about'),
]
