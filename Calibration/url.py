from django.urls import path
from Calibration import views

# TEMPLATE URLS!

app_name = 'calibration'


urlpatterns = [
    path('', views.cali_serv, name='cali_service'),
    path('instrument/', views.instr_serv, name='instrument_service'),
    path('automation/', views.auto_serv, name='automation_service'),
    path('pneumatic/', views.pneum_serv, name='pneumatic_service'),
    path('airco/', views.ac_serv, name='airco_service'),
    ]