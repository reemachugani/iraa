from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from config import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^art/', include('art.urls', namespace='art')),
    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^$', 'art.views.art_home', name='art_home'),

    url(r'^', include('singlepage.urls', namespace='singlepage')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)