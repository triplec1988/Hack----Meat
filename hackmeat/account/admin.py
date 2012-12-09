from django.contrib import admin
from models import *

class FarmerAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'farm_name', 'user_name', 'email', 'city', 'zipcode',)
	fields = ('first_name', 'last_name', 'farm_name', 'user_name', 'email', 'city', 'zipcode',)



class ProcessorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'plant_name', 'user_name', 'email', 'city', 'zipcode', 'resource', 'animal_spec', 'cut_spec', 'capacity',)
	fields = ('first_name', 'last_name', 'plant_name', 'user_name', 'email', 'city', 'zipcode', 'resource', 'animal_spec', 'cut_spec', 'capacity',)



class ResourceAdmin(admin.ModelAdmin):
	list_display = ('name',)
	fields = ('name',)



class FeeAdmin(admin.ModelAdmin):
	list_display = ('processor', 'slaughter', 'slaughter_fee', 'packaging', 'packaging_fee', 'processing', 'processing_fee',)
	fields = ('processor', 'slaughter', 'slaughter_fee', 'packaging', 'packaging_fee', 'processing', 'processing_fee',)




admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Processor, ProcessorAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Fee, FeeAdmin)