from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Author


class AuthorListView(ListView):
    model = Author
    ordering = ['pk']
    template_name = 'author_list.html'