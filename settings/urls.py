from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Botany

    # Filters
    #url(r'^sample_search/', views.sample_search, name='sample_search'),
    # see https://www.dev2qa.com/django-filter-and-pagination-example/

    # overviews
    # path('', views.allbotany, name='allbotany'),



path('overview/', views.overview, name='overview'),
path('overview/gygaia_samples_updated/', views.updategygaiasamplerows, name='updategygaiasamplerows')





]
