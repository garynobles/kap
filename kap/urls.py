from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from chat.views import index

import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('chat/', include('chat.urls', namespace='chat')),

    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),

    path('sample/', include('sample.urls')),
    path('botany/', include('botany.urls')),
	path('conservation/', include('conservation.urls')),
	path('zooarch/',include('zooarch.urls')),

    path('depot/',include(('depot.urls', 'depot'), namespace='depot')),

    #experimental
    path('experimental/', include('experimental.urls')),
    path('models3d/', include('models3d.urls')),

    path('spatial3d/', include('spatial3d.urls')),

    path('documentation/', include('documentation.urls')),
    path('teams/', include('teams.urls')),
    path('tickets/', include('tickets.urls')),
    path('settings/', include('settings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
