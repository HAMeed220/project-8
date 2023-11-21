from nz.views import *
from django.urls import path

app_name = 'kohili'

urlpatterns=[
    path('boomra/',boomra,name='boomra'),
    
]