from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:musicid>/', views.musicnum, name='musicid'),
    path('<int:year>/<int:month>/', views.musiclist, name='monthmusic'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', views.musiclist, name='monthmusic'),
]
