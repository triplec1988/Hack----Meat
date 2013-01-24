from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('hackmeat.base.views',
<<<<<<< HEAD
    url(r'^$', r'home', name='home')
=======
    url(r'^$', r'home'),
    url(r'^about/?$', r'about', name='about'),
    url(r'^contact/?$', r'contact', name='contact'),
    url(r'^contact_complete/?$', r'contact_complete', name='contact_complete'),
>>>>>>> 689b49e40fb468291135292e8ac4970ff45d0f14
)
