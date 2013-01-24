from django.contrib import admin
from models import *


class ReservationAdmin(admin.ModelAdmin):
	pass
admin.site.register(Reservation, ReservationAdmin)


class Cut_FormAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cut_Form, Cut_FormAdmin)
