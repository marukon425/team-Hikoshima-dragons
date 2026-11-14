from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Play._meta.fields]
    search_fields = [field.name for field in Play._meta.fields]

@admin.register(PlayTurn)
class PlayTurnAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlayTurn._meta.fields]
    search_fields = [field.name for field in PlayTurn._meta.fields]
