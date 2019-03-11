from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='postbin-home'),
    path('about/', views.about, name='postbin-about'),
]
