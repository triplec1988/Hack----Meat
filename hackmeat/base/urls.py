from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('hackmeat.base.views',
    url(r'^$', r'home', name='home')
)
