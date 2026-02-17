from django.contrib import admin
from .models import Game, Review
# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')
    search_fields = ('title',)
    
admin.site.register(Review)