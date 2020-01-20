from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:bookid>/', views.booknum, name='bookid'),
    path('<int:year>/<int:month>/', views.booklist, name='monthbook'),
    url(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', views.booklist, name='monthbook'),


]
