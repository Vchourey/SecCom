from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:movieid>/', views.movienum, name='movieid'),
    path('<int:year>/<int:month>/', views.movielist, name='monthmovies'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', views.movielist, name='monthmovies'),

]