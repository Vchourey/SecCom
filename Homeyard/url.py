from django.urls import path
from django.conf.urls import url
from Homeyard import views

# TEMPLATE URLS!

app_name = 'homeyard'

urlpatterns = [

#    path('', views.homeyard, name='homeyard'),
    path('', views.index, name='homeyard'),
    path('reg', views.register, name='register'),
    path('login', views.userlogin, name='userlogin'),
    path('logout', views.user_logout, name='logout'),

]
