from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'date_creation', 'publication_type', 'author')
    list_display_links = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat', 'description')
    list_display_links = ('name_cat',)


admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)
