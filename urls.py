from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name="home"),
    url(r'^submit$', views.submit, name="submit"),
    url(r'^actor/$', views.actor, name="actor_index"),
    url(r'^actor/(.*)$', views.actor, name="actor"),
    url(r'^meerkatter/(.*)$', views.meerkatter, name="meerkatter_index"),
    url(r'^meerkatter/$', views.meerkatter, name="meerkatter_index"),
    url(r'^register$', views.register, name="register"),
    (r'^admin$', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )


