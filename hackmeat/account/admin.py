from django.contrib import admin
from hackmeat.account.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'profiles'


class UserAdmin(UserAdmin):
	inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Farmer)
admin.site.register(Processor)
admin.site.register(Resource)
admin.site.register(Fee)
