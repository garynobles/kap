from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [

path('alltickets', views.alltickets, name='alltickets'),
path('opentickets', views.opentickets, name='opentickets'),
path('assignedtickets', views.assignedtickets, name='assignedtickets'),
path('closedtickets', views.closedtickets, name='closedtickets'),
path('allcompletedtickets', views.allcompletedtickets, name='allcompletedtickets'),
path('newticket', views.createticket, name='createticket'),
re_path(r'^deleteticket/(?P<pk>\d+)$', views.deleteticket, name='deleteticket'),
re_path(r'^ticket/edit/(?P<pk>\d+)/edit/$', views.editticket, name='editticket'),
path('ticket/<int:pk>/', views.detailticket, name='detailticket'),
]
