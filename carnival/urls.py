"""carnival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from user import views
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def page_not_found(request):
    return render(request, '404.html')


def server_error(request):
    return render(request, '500.html')


def bad_request(request):
    return render(request, '500.html')


urlpatterns = [
    path('', homepage),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    url(r'^user/', include('user.urls')),
]
