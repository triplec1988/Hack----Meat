from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('hackmeat.account.views',
    url(r'processors/(?P<zipcode>\d+)?/?$', r'processors'),
    url(r'signup/farmer/?$', r'signup_farmer'),
    url(r'signup/processor/?$', r'signup_processor'),
    url(r'settings/farmer/?$', r'settings_farmer'),
    url(r'settings/processor?$', r'settings_processor'),
    url(r'processor/(?P<processor>\d+)/?$', r'processor'),
)
