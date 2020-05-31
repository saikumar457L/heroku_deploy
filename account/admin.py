from django.contrib import admin

from .models import Profile,Marktry

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','photo']


@admin.register(Marktry)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['body']
