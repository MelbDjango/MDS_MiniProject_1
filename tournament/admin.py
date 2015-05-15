from django.contrib import admin
from .models import Tournament, Player, Match


class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'start', 'player_max', 'current']
    list_filter = ['name']

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Player)
admin.site.register(Match)

# Register your models here.
