from django.contrib import admin

from blog.models import Blog, Author


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'picture',)
    list_filter = ('title', 'author',)
    search_fields = ('title', 'content', 'author')



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name',)
    list_filter = ('author_name',)
    search_fields = ('author_name',)
