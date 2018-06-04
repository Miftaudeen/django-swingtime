import os
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

admin.autodiscover()
doc_root = os.path.join(os.path.dirname(settings.PROJECT_DIR), 'docs/build/html')

urlpatterns = ['',
               path('^$', TemplateView, {'template': 'intro.html'}, name='demo-home'),
               path(r'^karate/', include('karate.urls')),
               path(r'^admin/docs/', include('django.contrib.admindocs.urls')),
               path(r'^admin/', include(admin.site.urls)),
               path(r'^docs/?$', RedirectView, dict(url='/docs/index.html')),
               path(r'^docs/(?P<path>.*)$', serve, dict(document_root=doc_root, show_indexes=False))
               ]

if settings.DEBUG:
    data = dict(document_root=settings.MEDIA_ROOT, show_indexes=True)
    urlpatterns += ['',
                    path(r'^media/(?P<path>.*)$', serve, data),
                    ]
