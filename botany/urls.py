from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    #Botany
    path('', views.allbotany, name='allbotany'),

    path('flotation/', views.allflotation, name='allflotation'),
    path('flotation/<int:botany_id>', views.allflotation, name='allflotation'),

    # url(r'^project_config/$', views.foo),
    # url(r'^project_config/(?P<product>\w+)/$', views.foo),
    # ulr(r'^project_config/(?P<product>\w+)/(?P<project_id>\w+)/$', views.foo),
    # path('flotation/', views.allflotationfilter, name='allflotationfilter'),
    path('addflotation/', views.addflotation, name='addflotation'),
    re_path('addflotation/(?P<pk>\d+)/', views.addflotation, name='addflotation'),





    path('sample/flotation/<int:botany_id>/', views.detailflotation, name='detailflotation'),
    re_path('flotation/edit/(?P<pk>\d+)/edit/', views.editflotation, name='editflotation'),

    ##
    path('sample/', views.allsample, name='allsample'),
    path('addsample/', views.addsample, name='addsample'),
    path('sample/<int:sample_id>/', views.detailsample, name='detailsample'),
    re_path('sample/edit/(?P<pk>\d+)/edit/', views.editsample, name='editsample'),

    ##
    # url(r'^sample/$', views.addfraction, name='addfraction'),
    # url(r'^sample/(?P<sample_id>\w+)/$', views.addfraction, name='addfraction'),
    # url(r'^sample/(?P<sample_id>\w+)/flotation/$', views.addfraction, name='addfraction'),
    # url(r'^sample/(?P<sample_id>\w+)/flotation/(?P<pk>\d+)/$', views.addfraction, name='addfraction'),

    re_path(r'^flotation/(?P<pk>\d+)/$', views.addfraction, name='addfraction'),

# url(r'^flotation/(?P<pk>\d+)/$', views.addfraction, name='addfraction'),

    re_path(r'^sample/(?P<fk>\d+)/flotation/(?P<pk>\d+)/$', views.addfraction, name='addfraction'),

    re_path(r'^flotation/(?P<fk>\d+)/addcomposition/(?P<pk>\d+)/$', views.addcomposition, name='addcomposition'),

    path('flotation/<int:botany_id>/fraction/<int:fraction_id>/', views.detailfraction, name='detailfraction'),
    re_path('flotation/(?P<fk>\d+)/fraction/edit/(?P<pk>\d+)/edit/', views.editfraction, name='editfraction'),

    # url(r'^(?P<fk>\d+)/addmaterialpresent/(?P<pk>\d+)/$', views.addmaterialpresent, name='addmaterialpresent'),
    #url(r'^(?P<fk>\d+)/fraction/(?P<pk>\d+)/$', views.detailfraction, name='detailfraction'),
    #url(r'^(?P<pk>\d+)/fraction/(?P<fk>\d+)/$', views.detailfraction, name='detailfraction'),
    #path('createfraction/(?P<pk>\d+)/', views.createfraction, name='createfraction'),
    #path('botany/(?P<pk>\d+)/', views.createfraction, name='createfraction'),
    # path('fraction/', views.allfraction, name='allfraction'),
    #path('fractioncomposition/', views.allfractioncomposition, name='allfractioncomposition'),
    #path('fractionmaterialpresent/', views.allfractionmaterialpresent, name='allfractionmaterialpresent'),
    #path('addcomposition/', views.addcomposition, name='create_fractioncomposition'),
    #path('createfractionmaterialpresent/', views.createfractionmaterialpresent, name='create_fractionmaterialpresent'),
    #path('detailfractioncomposition/<int:fract_comp_id>/', views.detailfractioncomposition, name='detailfractioncomposition'),
    #path('detailfractionmaterialpresent/<int:material_id>/', views.detailfractionmaterialpresent, name='detailfractionmaterialpresent'),



]
