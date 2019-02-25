from django.urls import path, re_path
from django.conf.urls import url

from .views import models3d

urlpatterns = [

path('', models3d, name='models3d'),


]
