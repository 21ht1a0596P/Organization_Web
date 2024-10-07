from django.contrib import admin
from django.urls import path
from main import views  # Import views from the main app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('placements/', views.placements, name='placements'),
    path('materials/', views.materials, name='materials'),
    path('results/', views.results, name='results'),
]
