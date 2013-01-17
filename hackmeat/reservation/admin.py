from django.contrib import admin
from models import *


class ReservationAdmin(admin.ModelAdmin):
	pass
admin.site.register(Reservation, ReservationAdmin)


class Animal_ReservationAdmin(admin.ModelAdmin):
	pass
admin.site.register(Animal_Reservation, Animal_ReservationAdmin)


class Cut_FormAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cut_Form, Cut_FormAdmin)
