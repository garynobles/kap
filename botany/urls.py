from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.allbotany, name='allbotany'),
    path('flotation/', views.allflotation, name='allflotation'),

    path('addflotation/', views.addflotation, name='createflotation'),
    url(r'^addfraction/(?P<pk>\d+)/$', views.addfraction, name='addfraction'),


    url(r'^(?P<fk>\d+)/addcomposition/(?P<pk>\d+)/$', views.addcomposition, name='addcomposition'),
    url(r'^(?P<fk>\d+)/addmaterialpresent/(?P<pk>\d+)/$', views.addmaterialpresent, name='addmaterialpresent'),


    path('<int:botany_id>/', views.detailbotany, name='detailbotany'),



    path('<int:botany_id>/fraction/<int:fraction_id>/', views.detailfraction, name='detailfraction'),
    #url(r'^(?P<fk>\d+)/fraction/(?P<pk>\d+)/$', views.detailfraction, name='detailfraction'),
    #url(r'^(?P<pk>\d+)/fraction/(?P<fk>\d+)/$', views.detailfraction, name='detailfraction'),


    #path('createfraction/(?P<pk>\d+)/', views.createfraction, name='createfraction'),
    # path('botany/(?P<pk>\d+)/', views.createfraction, name='createfraction'),
    #
    #
    #
    #
    #
     #path('fraction/', views.allfraction, name='allfraction'),
    #
    # path('fractioncomposition/', views.allfractioncomposition, name='allfractioncomposition'),
    # path('fractionmaterialpresent/', views.allfractionmaterialpresent, name='allfractionmaterialpresent'),
    #
    #
    #

    #
    #
    #
    # path('addcomposition/', views.addcomposition, name='create_fractioncomposition'),
    # path('createfractionmaterialpresent/', views.createfractionmaterialpresent, name='create_fractionmaterialpresent'),
    #
    # path('detailfractioncomposition/<int:fract_comp_id>/', views.detailfractioncomposition, name='detailfractioncomposition'),
    # path('detailfractionmaterialpresent/<int:material_id>/', views.detailfractionmaterialpresent, name='detailfractionmaterialpresent'),
    #
    #
    # path('fraction/edit/(?P<pk>\d+)/edit/', views.editfraction, name='editfraction'),
]
