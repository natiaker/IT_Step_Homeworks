"""
URL configuration for eventmanagerapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_user, name='logout_user'),
    path('add_event/', views.add_event, name='add_event'),
    path('remove_event/<int:event_id>/', views.remove_event, name='remove_event')
]
