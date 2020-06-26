"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views



urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('list_professor/', views.list_professor, name = 'list_prof'),
    path('cadastro_professor/', views.professor, name='form_prof'),
    path('update_prof/<int:pk>/', views.update_prof, name='up_prof'),
    path('list_professor/delete_prof/<int:pk>/', views.del_prof, name='delete_prof'),
]
