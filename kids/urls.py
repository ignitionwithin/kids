from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from oscar.app import application
from django.contrib import admin

from kids import settings


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'kids.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'', include(application.urls)),
                       url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

