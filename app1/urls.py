from django.urls import path
from django.urls.resolvers import URLPattern
from app1.views import *

app_name='app_1'

urlpatterns=[
    path('app1_fun1/',app1_fun1,name='app1_fun1'),
]