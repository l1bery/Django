from django.contrib import admin

from apps.articles.models import Genre,Game,Review



@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'developer', 'publisher', 'age_rating')
    search_fields = ('title', 'developer', 'publisher')
    list_filter = ('release_date', 'age_rating', 'developer', 'publisher', 'genres')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('genres',)  # удобное отображение жанров

    def game_count(self, obj):
        return obj.game_set.count()  # Показывает кол-во игр в жанре
