from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('hackmeat.reservation.views',
	url(r'^processor_reserve/?$', r'processor_reserve'),
	url(r'^order/?$', r'order'),
	url(r'^confirmation/?$', r'confirmation')
)
