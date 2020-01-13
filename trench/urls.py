from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.alltrenches, name='alltrenches'),
    path('addtrench/', views.addtrench, name='addtrench'),
    path('<int:trench_id>', views.detailtrench, name='detailtrench'),

    re_path('(?P<pk>\d+)/', views.edittrench, name='edittrench'),
]
