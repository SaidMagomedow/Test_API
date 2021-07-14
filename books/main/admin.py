from django.contrib import admin

# Register your models here.
from .models import Books, Author


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'title', 'description']
    list_filter = ['author__name']
    search_fields = ['title']



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'country']
    list_filter = ['country']
    search_fields = ['books__title']


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'description']
    list_filter = ['author__name']
    search_fields = ['title']
