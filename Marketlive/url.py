from django.urls import path
from django.conf.urls import url
from . import views
from Marketlive.views import static_list, static_temp

urlpatterns = [

    path('', views.market, name='Marketlive'),
    path('staticview/', static_temp.as_view(), name='staticview'),
    path('listview/', static_list.as_view(template_name = 'Market_html/Liveupdate.html'), name='listview'),

]