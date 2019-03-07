from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Botany
    # overviews
    path('', views.allbotany, name='allbotany'),
    path('sample/', views.allsample, name='allsample'),

    # path('botany', views.botanyview, name='botanyview'),
    path('botanyoverview/sample/<int:sample_id>/flotation/<int:flotation_id>', views.botanyoverview, name='botanyoverview'),

    path('sample/flotation/', views.allflotation, name='allflotation'),
    path('flotation/<int:flotation_id>', views.allflotation, name='allflotation'),

    # listviews
    path('samplelist/', views.SampleListView.as_view(), name='samplelist'),

    # add
    path('addsample/', views.addsample, name='addsample'),

    re_path(r'^sample/addflotation/(?P<pk>\d+)/$', views.addflotation, name='addflotation'),
    re_path(r'^flotation/(?P<pk>\d+)/$', views.addlightresidue, name='addlightresidue'),
    re_path(r'^sample/(?P<fk>\d+)/flotation/(?P<pk>\d+)/$', views.addlightresidue, name='addlightresidue'),
    re_path(r'^sample/(?P<sp>\d+)/flotation/(?P<fk>\d+)/addcomposition/(?P<pk>\d+)/$', views.addcomposition, name='addcomposition'),



    re_path('sample/(?P<sp>\d+)/flotation/(?P<fl>\d+)/lightresidue/(?P<fk>\d+)/composition/(?P<pk>\d+)/addfraction/', views.addfraction, name='addfraction'),
    re_path('sample/(?P<sp>\d+)/flotation/(?P<fl>\d+)/composition/(?P<fk>\d+)/fraction/(?P<pk>\d+)/addplantpart/', views.addplantpart, name='addplantpart'),

    # edit
    re_path('sample/edit/(?P<pk>\d+)/edit/', views.editsample, name='editsample'),

    re_path('flotation/edit/(?P<pk>\d+)/edit/', views.editflotation, name='editflotation'),
    re_path('sample/(?P<fk>\d+)/flotationform/edit/(?P<pk>\d+)/edit/', views.editflotationform, name='editflotationform'),


    re_path('sample/(?P<sp>\d+)/flotation/(?P<fk>\d+)/lightresidue/edit/(?P<pk>\d+)/edit/', views.editlightresidue, name='editlightresidue'),
    re_path('sample/(?P<sp>\d+)/flotation/(?P<fl>\d+)/lightresidue/(?P<fk>\d+)/composition/edit/(?P<pk>\d+)/edit/', views.editcomposition, name='editcomposition'),


    # re_path('flotation/(?P<fk>\d+)/lightresidue/edit/(?P<pk>\d+)/edit/', views.editfraction, name='editfraction'),


    re_path('sample/(?P<sp>\d+)/flotation/(?P<fl>\d+)/composition/(?P<fk>\d+)/fraction/edit/(?P<pk>\d+)/edit/', views.editfraction, name='editfraction'),

    re_path('sample/(?P<sp>\d+)/flotation/(?P<fl>\d+)/fraction/(?P<fk>\d+)/plantpart/edit/(?P<pk>\d+)/edit/', views.editplantpart, name='editplantpart'),



    # details
    path('sample/<int:sample_id>/', views.detailsample, name='detailsample'),
    path('sample/flotation/<int:flotation_id>/', views.detailflotation, name='detailflotation'),
    path('flotation/lightresidue/<int:lightresidue_id>/', views.detaillightresidue, name='detaillightresidue'),
    # path('sample/flotation/lightresidue/<int:lightresidue_id>/', views.detaillightresidue, name='detaillightresidue'),

    path('flotation/lightresidue/<int:lightresidue_id>/composition/<int:composition_id>/', views.detailcomposition, name='detailcomposition'),

    path('flotation/composition/<int:composition_id>/fraction/<int:fraction_id>/', views.detailfraction, name='detailfraction'),



# path('addflotation/', views.addflotation, name='addflotation'),





]
