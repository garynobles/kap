from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),



    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),

    path('botany/', include('botany.urls')),
    #path('zooarch/', include('zooarch.urls')),
    path('spatial3d/', include('spatial3d.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
