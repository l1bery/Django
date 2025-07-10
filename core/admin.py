from django.contrib import admin

from apps.articles.models import Genre,Game,Review

# admin.site.register(PlaceCategory)
# admin.site.register(Place)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'game_count')
    search_fields = ('name',)
    list_display_links = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}  # Автозаполнение slug

    def game_count(self, obj):
        return obj.game_set.count()  # Показывает кол-во игр в жанре