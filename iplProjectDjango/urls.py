"""
URL configuration for iplProjectDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from problems import views

urlpatterns = [
    path("", views.home),
    path('matches-count/', views.matches_played),
    path('matches-won/', views.matches_won),
    path('extra-runs/<int:year>/', views.extra_runs),   # dynamic-urls
    path('economical-bowlers/<int:year>/<int:count>/', views.economical_bowlers), 
    path('matches-count-chart/', views.matches_played_chart),
    path('matches-won-chart/', views.matches_won_chart),
    path('extra-runs-chart/<int:year>/', views.extra_runs_chart),   # dynamic-urls
    path('economical-bowlers-chart/<int:year>/<int:count>/', views.economical_bowlers_chart), 
    path('admin/', admin.site.urls),
]
