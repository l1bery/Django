from django.contrib import admin

from apps.articles.models import Genre,Game,Review



@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'developer', 'age_rating')
    search_fields = ('title',)
    list_filter = ('release_date', 'age_rating', 'developer', 'genres')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('genres',)  # удобное отображение жанров



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'rating', 'created_time')
    search_fields = ('user_name',)
    list_filter = ('rating', 'created_time')
    ordering = ('-created_time',)
    readonly_fields = ('created_time',)