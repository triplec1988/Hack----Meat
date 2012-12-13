from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('hackmeat.account.views',
    url(r'processors/(?P<zipcode>\d+)/?$', r'processors'),
    url(r'signup/farmer/?$', r'signup_farmer'),
    url(r'signup/processor/?$', r'signup_processor'),
    url(r'settings/farmer/?$', r'settings_farmer'),
    url(r'settings/processor?$', r'settings_processor'),
    url(r'processor/(?P<processor>\d+)/?$', r'processor'),
    url(r'farmer/dashboard/$', direct_to_template, {'template': 'account/farmer_dashboard.html'}),
    url(r'processor/dashboard/$', direct_to_template, {'template': 'account/processor_dashboard.html'}),
    #About URLs
    url(r'processors/about/$', direct_to_template, {'template': 'base/about.html'}),
    url(r'^signup/about/?$', r'about', name='about'),
    #Contact URLs
    url(r'^processors/contact/?$', r'contact', name='contact'),
    url(r'^farmer/dashboard/contact/?$', r'contact', name='contact'),
    url(r'^processor/dashboard/contact/?$', r'contact', name='contact'),
    url(r'^signup/contact/?$', r'contact', name='contact'),
)
