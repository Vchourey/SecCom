"""Vijayweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import Homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Homeyard.url')),
    path('calibration/', include('Calibration.url')),
    path('enquiry/', include('Enquiry.url')),
    path('contact/', include('Enquiry.url')),
#   path('', Homeview.home, name='home'),
    path('movies/', include('Movies.url')),
    path('music/', include('Music.url')),
    path('books/', include('Books.url')),
    path('mylearning/', include('Mylearning.url')),
    path('marketlive/', include('Marketlive.url')),
    path('admin/', admin.site.urls),
#    path('', include('Homeapp.url')),
#    path('home/', include('pages.urls')),
#    path('listings/', include('listings.urls')),
#    path('accounts/', include('accounts.urls')),
#    path('contacts/', include('contacts.urls')),

]