from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile
# Register your models here.

#admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'anzahlPersonenAlt', 'anzahlPersonenJung')
    list_filter = ('status', 'anzahlPersonenAlt', 'anzahlPersonenJung')
    ordering = ('status', )
    search_fields = ('user__username',)
# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)