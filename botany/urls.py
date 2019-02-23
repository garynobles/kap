from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    #Botany
    path('', views.allbotany, name='allbotany'),

    path('flotation/', views.allflotation, name='allflotation'),
    path('flotation/<int:flotation_id>', views.allflotation, name='allflotation'),

    # url(r'^project_config/$', views.foo),
    # url(r'^project_config/(?P<product>\w+)/$', views.foo),
    # ulr(r'^project_config/(?P<product>\w+)/(?P<project_id>\w+)/$', views.foo),
    # path('flotation/', views.allflotationfilter, name='allflotationfilter'),
    path('addflotation/', views.addflotation, name='addflotation'),
    re_path('addflotation/(?P<pk>\d+)/', views.addflotation, name='addflotation'),



    # listview test
    path('samplelist/', views.SampleListView.as_view(), name='samples'),




    path('sample/flotation/<int:flotation_id>/', views.detailflotation, name='detailflotation'),
    re_path('flotation/edit/(?P<pk>\d+)/edit/', views.editflotation, name='editflotation'),

    ##

    path('sample/', views.allsample, name='allsample'),

    path('addsample/', views.addsample, name='addsample'),
    path('sample/<int:sample_id>/', views.detailsample, name='detailsample'),
    re_path('sample/edit/(?P<pk>\d+)/edit/', views.editsample, name='editsample'),

    ##
    # url(r'^sample/$', views.addlightresidue, name='addlightresidue'),
    # url(r'^sample/(?P<sample_id>\w+)/$', views.addlightresidue, name='addlightresidue'),
    # url(r'^sample/(?P<sample_id>\w+)/flotation/$', views.addlightresidue, name='addlightresidue'),
    # url(r'^sample/(?P<sample_id>\w+)/flotation/(?P<pk>\d+)/$', views.addlightresidue, name='addlightresidue'),

    re_path(r'^flotation/(?P<pk>\d+)/$', views.addlightresidue, name='addlightresidue'),

# url(r'^flotation/(?P<pk>\d+)/$', views.addlightresidue, name='addlightresidue'),

    re_path(r'^sample/(?P<fk>\d+)/flotation/(?P<pk>\d+)/$', views.addlightresidue, name='addlightresidue'),

    re_path(r'^flotation/(?P<fk>\d+)/addcomposition/(?P<pk>\d+)/$', views.addcomposition, name='addcomposition'),

    path('flotation/<int:flotation_id>/lightresidue/<int:fraction_id>/', views.detaillightresidue, name='detaillightresidue'),
    re_path('flotation/(?P<fk>\d+)/lightresidue/edit/(?P<pk>\d+)/edit/', views.editfraction, name='editfraction'),

    # url(r'^(?P<fk>\d+)/addmaterialpresent/(?P<pk>\d+)/$', views.addmaterialpresent, name='addmaterialpresent'),
    #url(r'^(?P<fk>\d+)/lightresidue/(?P<pk>\d+)/$', views.detaillightresidue, name='detaillightresidue'),
    #url(r'^(?P<pk>\d+)/lightresidue/(?P<fk>\d+)/$', views.detaillightresidue, name='detaillightresidue'),
    #path('createfraction/(?P<pk>\d+)/', views.createfraction, name='createfraction'),
    #path('botany/(?P<pk>\d+)/', views.createfraction, name='createfraction'),
    # path('lightresidue/', views.allfraction, name='allfraction'),
    #path('composition/', views.allcomposition, name='allcomposition'),
    #path('fractionmaterialpresent/', views.allfractionmaterialpresent, name='allfractionmaterialpresent'),
    #path('addcomposition/', views.addcomposition, name='create_composition'),
    #path('createfractionmaterialpresent/', views.createfractionmaterialpresent, name='create_lightresiduematerialpresent'),
    #path('detailcomposition/<int:fract_comp_id>/', views.detailcomposition, name='detailcomposition'),
    #path('detaillightresiduematerialpresent/<int:material_id>/', views.detaillightresiduematerialpresent, name='detaillightresiduematerialpresent'),



]
