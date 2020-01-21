from django.urls import path
from Calibration import views

# TEMPLATE URLS!

app_name = 'calibration'


urlpatterns = [
    path('', views.cali_serv, name='cali_service'),

    ]