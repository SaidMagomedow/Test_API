from django.contrib import admin

# Register your models here.
from .models import Books, Users


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'title', 'description']
    list_filter = ['author__first_name']
    search_fields = ['title']


@admin.register(Users)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'country']
    list_filter = ['country']
    search_fields = ['books__title']


