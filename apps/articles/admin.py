from django.contrib import admin

from apps.articles.models import Genre,Game,Review



@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date','price',)
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_filter = ('release_date',)
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    # filter_horizontal = ('genres',)  # удобное отображение жанров



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'rating', 'created_time')
    search_fields = ('user_name',)
    list_filter = ('rating', 'created_time')
    ordering = ('-created_time',)
    readonly_fields = ('created_time',)