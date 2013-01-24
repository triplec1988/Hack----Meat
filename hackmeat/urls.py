from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('hackmeat.base.urls')),
    url(r'^u/', include('hackmeat.account.urls')),
    url(r'^r/', include('hackmeat.reservation.urls')),
    #url(r'^accounts/', include('django.contrib.auth.urls'))
    url(r'^accounts/login/$', 'hackmeat.account.views.login_view', name='login'),
    url(r'^accounts/logout/$', 'hackmeat.account.views.logout_view', )

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)


if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
