from django.contrib import admin

from .models import Category, Location, Post


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'pub_date',
        'location',
        'author',
        'category',
        'text'
    )
    list_editable = ('is_published', 'category',)
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'


# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post, BlogAdmin)
