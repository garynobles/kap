from django.urls import path
from django.conf.urls import url

from . import views

#from zooarch.views import ZooarchListView, QnispListView

urlpatterns = [
    #zooarch

    ##path('samples/', ZooarchListView.as_view(template_name="zooarch/allzooarch.html"), name='allzooarch'),
    #path('', ZooarchListView.as_view(template_name="zooarch/allzooarch.html"), name='allzooarch'),
     #path('zooarch/<int:sample_id>/', views.detailzooarch, name='detailzooarch'),
     #url(r'^zooarch/edit/(?P<pk>\d+)/edit/$', views.editzooarch, name='editzooarch'),
#     url(r'^zooarch/createzooarch/$', views.createzooarch, name='createzooarch'),
#
#
#     path('zooarch/<int:sample_id>/', views.detailzooarch, name='detailzooarch'),
#
    #qnisp
    path('', views.allzooarch, name='allzooarch'),

    path('qnisp/', views.allqnisp, name='allqnisp'),
    url(r'^qnisp/createqnisp/$', views.createqnisp, name='createqnisp'),

    #path('qnisp/', QnispListView.as_view(template_name="qnisp/allqnisp.html"), name='allqnisp'),
#path('fractioncomposition/', views.allfractioncomposition, name='allfractioncomposition'),

    path('qnisp/<int:qnisp_id>/', views.detailqnisp, name='detailqnisp'),
    # #

    url(r'^qnisp/edit/(?P<pk>\d+)/edit/$', views.editqnisp, name='editqnisp'),
    # #
    url(r'^qnisp/(?P<pk>\d+)$', views.removeqnisp, name='removeqnisp'),




]
