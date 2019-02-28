from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Botany
    # overviews
    path('', views.allbotany, name='allbotany'),
    path('sample/', views.allsample, name='allsample'),

    path('sample/flotation/', views.allflotation, name='allflotation'),
    path('flotation/<int:flotation_id>', views.allflotation, name='allflotation'),

    # listviews
    path('samplelist/', views.SampleListView.as_view(), name='samplelist'),

    # add
    path('addsample/', views.addsample, name='addsample'),

    re_path(r'^sample/addflotation/(?P<pk>\d+)/$', views.addflotation, name='addflotation'),
    re_path(r'^flotation/(?P<pk>\d+)/$', views.addlightresidue, name='addlightresidue'),
    re_path(r'^sample/(?P<fk>\d+)/flotation/(?P<pk>\d+)/$', views.addlightresidue, name='addlightresidue'),
    re_path(r'^flotation/(?P<fk>\d+)/addcomposition/(?P<pk>\d+)/$', views.addcomposition, name='addcomposition'),

    # details
    path('sample/<int:sample_id>/', views.detailsample, name='detailsample'),
    path('sample/flotation/<int:flotation_id>/', views.detailflotation, name='detailflotation'),
    path('flotation/lightresidue/<int:lightresidue_id>/', views.detaillightresidue, name='detaillightresidue'),
    # path('sample/flotation/lightresidue/<int:lightresidue_id>/', views.detaillightresidue, name='detaillightresidue'),

    # edit
    re_path('sample/edit/(?P<pk>\d+)/edit/', views.editsample, name='editsample'),
    re_path('flotation/edit/(?P<pk>\d+)/edit/', views.editflotation, name='editflotation'),
    re_path('flotation/(?P<fk>\d+)/lightresidue/edit/(?P<pk>\d+)/edit/', views.editlightresidue, name='editlightresidue'),
    re_path('flotation/(?P<fk>\d+)/lightresidue/edit/(?P<pk>\d+)/edit/', views.editfraction, name='editfraction'),



# path('addflotation/', views.addflotation, name='addflotation'),





]
