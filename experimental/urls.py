from django.urls import path
from django.conf.urls import url

from . import views

#from spatial3d.views import PhotobatchListView

urlpatterns = [
    #path('fraction/', views.allfraction, name='allfraction'),
    #photobatch

    #url(r'^""$', PhotobatchListView.as_view(template_name="photobatch/allphotobatch.html"), name='allphotobatch'),
    #path('photobatch/', PhotobatchListView.as_view(template_name="photobatch/allphotobatch.html"), name='allphotobatch'),

    path('webviewer3d/', views.webviewer3d, name='webviewer3d'),

    # path('pointcloud2volume/', views.Pointcloud2Volume, name='pointcloud2volume'),
    # path('photobatch/<int:sample_id>/', views.detailphotobatch, name='detailphotobatch'),
    # url(r'^photobatch/edit/(?P<pk>\d+)/edit/$', views.editphotobatch, name='editphotobatch'),
    # url(r'^photobatch/createphotobatch/$', views.createphotobatch, name='createphotobatch'),
    # #
    # #url(r'^photobatch/remove/(?P<pk>\d+)/remove/$', views.removephotobatch, name='removephotobatch'),
    # #path('photobatch/<int:pk>/delete/', views.removephotobach.as_view(), name='removephotobatch'),
    # url(r'^photobatch/(?P<pk>\d+)$', views.removephotobatch, name='removephotobatch'),
]
