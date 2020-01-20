from django.urls import path
from django.conf.urls import url
from . import views


# TEMPLATE TAGGING
app_name = 'Mylearning'


urlpatterns = [

    path('', views.Mylearning, name='Mylearning'),
    path('InterviewQuestion/', views.InterviewQuestion, name='InterviewQuestion'),
    path('InterviewQA/', views.InterviewQuestionAnswer.as_view(), name='InterviewQuestionAnswer'),
    path(r'reg/', views.StudentReg, name='StudentReg'),

]
