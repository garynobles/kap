from django.urls import path, re_path
from django.conf.urls import url

from .views import detailstorage, allstorage, createstorage, editstorage, alllocation, detaillocation, createlocation, editlocation
from . import views

# from depot.views import SamplesListView, ContainerListView, LocationListView, JoinSampleContainerListView

urlpatterns = [

url(r'^container/(?P<operation>.*)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
# url(r'^containerx/<int:container_id>/(?P<operation>.*)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),

# EDIT

url(r'^storage/edit/(?P<pk>\d+)/edit/$', editstorage, name='editstorage'),
url(r'^location/edit/(?P<pk>\d+)/edit/$', editlocation, name='editlocation'),

#storage
re_path(r'^storage/$', allstorage, name='allstorage'),
path('storage/<int:store_id>/', detailstorage, name='detailstorage'),
#
url(r'^storage/createstorage/$', createstorage, name='createstorage'),


#locations
url(r'^location/$', alllocation, name='alllocation'),
path('location/<int:location_id>/', detaillocation, name='detaillocation'),
url(r'^createlocation/$', createlocation, name='createlocation'),


#container
url(r'^container/$', views.allcontainer, name='allcontainer'),
path('container/<int:container_id>/', views.detailcontainer, name='detailcontainer'),
# path('container/contents/<int:container_id>/', views.containercontents, name='containercontents'),
re_path(r'^editcontainercontents/edit/(?P<pk>\d+)/edit/$', views.editcontainercontents, name='editcontainercontents'),

re_path(r'^container/createcontainer/$', views.createcontainer, name='createcontainer'),
url(r'^container/edit/(?P<pk>\d+)/edit/$', views.editcontainer, name='editcontainer'),
# url(r'^container/search/edit/(?P<pk>\d+)/edit/$', views.editcontainersearch, name='editcontainersearch'),


# sample
path('alldepotsample', views.alldepotsample, name='alldepotsample'),
# path('alldepotsample/', views.SampleListView.as_view(), name='alldepotsample'),
re_path('assignsample/edit/(?P<pk>\d+)/edit/', views.assignsample, name='assignsample'),
path('sample/<int:sample_id>/', views.detaildepotsample, name='detaildepotsample'),
re_path('depotsample/edit/(?P<pk>\d+)/edit/', views.editdepotsample, name='editdepotsample'),
path('adddepotsample/', views.adddepotsample, name='adddepotsample'),
# path('containercontents/', views.containercontents, name='containercontents'),




# path('containercontentsdetail', views.containercontentsdetail, name='containercontentsdetail'),

# path('containerre_path(r'^containercontents/edit/(?P<pk>\d+)/edit/$', views.containercontents, name='containercontents'),contents/<int:pk>/', views.containercontents, name='containercontents'),


# url(r'^samples/filter/$', views.samplesearch, name='samplesearch'),
# url(r'^container/filter/$', views.containersearch, name='containersearch'),

# url(r'^container/page/$', views.containerpage, name='containerpage'),

# url(r'^samples/listing/$', views.listing, name='listing'),


# url(r'^sample_container_join/$', views.create_join_sample_container, name='create_join_sample_container'),
# url(r'^join_sample_container/create_join_sample_container/$', views.create_join_sample_container, name='create_join_sample_container'),
# url(r'^join_sample_container/edit/(?P<pk>\d+)/edit/$', views.edit_join_sample_container, name='edit_join_sample_container'),


# re_path(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),


]
