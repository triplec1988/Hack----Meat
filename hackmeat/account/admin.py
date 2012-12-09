from django.contrib import admin
from models import *
from hackmeat.account.models import Farmer, Processor, Resource, Fee

admin.site.register(Farmer)
admin.site.register(Processor)
admin.site.register(Resource)
admin.site.register(Fee)
