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



# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'game', 'rating', 'created_at')
#     search_fields = ('user_name', 'game__title')
#     list_filter = ('rating', 'created_at', 'game')
#     ordering = ('-created_at',)
#     readonly_fields = ('created_at',)