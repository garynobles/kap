from django.urls import path
from django.conf.urls import url

from . import views

from depot.views import SamplesListView, ContainerListView, LocationListView, JoinSampleContainerListView

urlpatterns = [
    #samples
    #path('samples/', views.SamplesListView, name='SamplesListView'),
    url(r'^samples/$', SamplesListView.as_view(template_name="samples/alldepotsamples.html"), name='alldepotsamples'),
    url(r'^container/$', ContainerListView.as_view(template_name="container/allcontainer.html"), name='allcontainer'),
    url(r'^location/$', LocationListView.as_view(template_name="location/alllocation.html"), name='alllocation'),

    url(r'^sample_container_join/$', JoinSampleContainerListView.as_view(template_name="join_sample_container/all_sample_container_joins.html"), name='all_sample_container_joins'),

    #url(r'^$', CurrencyListView.as_view()),
    #url(r'^createstore/$', views.createstore, name='createstore'),

    #url(r'^samples/$', SamplesListView.as_view(template_name="currencies/currency_filter.html")),


    #url(r'^samples/$', views.alldepotsamples, name='alldepotsamples'),

    path('samples/<int:sample_id>/', views.detailsamples, name='detailsamples'),
    url(r'^samples/edit/(?P<pk>\d+)/edit/$', views.editsample, name='editsample'),
    url(r'^samples/createsample/$', views.createsample, name='createsample'),

    


    path('container/<int:container_id>/', views.detailcontainer, name='detailcontainer'),

    path('container/<int:container_id>/', views.checked_out, name='checked_out'),

    #store
    # path('store/', views.allstorage, name='allstorage'),
    # path('<int:store_id>/', views.detailstore, name='detailstore'),
    #
    # url(r'^createstore/$', views.createstore, name='createstore'),
    # url(r'^editstore/(?P<pk>\d+)/editstore/$', views.editstore, name='editstore'),


    #url(r'^location/edit/(?P<pk>\d+)/edit/$', views.editlocation, name='editlocation'),







    #samples
    #url(r'^samples/$', views.alldepotsamples, name='alldepotsamples'),
    #path('samples/<int:sample_id>/', views.detailsamples, name='detailsamples'),

    #url(r'^samples/createsample/$', views.createsample, name='createsample'),
    #url(r'^samples/edit/(?P<pk>\d+)/edit/$', views.editsample, name='editsample'),


    #filtering and pagination
    #url(r'^container/search/$', views.containerfilterpage, name='containerfilterpage'),

    #pagination only
    #url(r'^users/page/$', views.index, name='index'),
    #filtering only



]
