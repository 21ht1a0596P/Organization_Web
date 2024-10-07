from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('placements/', views.placements, name='placements'),
    path('materials/', views.materials, name='materials'),
    path('results/', views.results, name='results'),
]
