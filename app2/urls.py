from django.urls import path
from app2.views import *

app_name='app_2'

urlpatterns=[
    path('app2_fun2/',app2_fun2,name='app2_fun2'),
]