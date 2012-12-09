from django.contrib import admin
from models import *


class ReservationAdmin(admin.ModelAdmin):
	list_display = ('farmer', 'processor', 'instruction', 'dropoff_time', 'pickup_time', 'status', )
	fields = ('farmer', 'processor', 'instruction', 'dropoff_time', 'pickup_time', 'status', )


class BlackoutAdmin(admin.ModelAdmin):
	list_display = ('processor', 'start_time', 'end_time', 'reason', )
	fields = ('processor', 'start_time', 'end_time', 'reason', )


class Animal_ReservationAdmin(admin.ModelAdmin):
	list_display = ('reservation', 'animal', 'animal_quantity', 'cut',)
	fields = ('reservation', 'animal', 'animal_quantity', 'cut',)


class AnimalAdmin(admin.ModelAdmin):
	list_display = ('name',)
	fields = ('name',)

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Blackout, BlackoutAdmin)
admin.site.register(Animal_Reservation, Animal_ReservationAdmin)
admin.site.register(Animal, AnimalAdmin)
