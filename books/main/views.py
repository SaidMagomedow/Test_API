from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import QueryAndSerializeMixin
from .models import Author, Books
from .serializers import BooksDeleteSerializer, BooksSerializer

from .models import Author


class AuthorListView(ListView):
    """
    Вывод всех авторов
    """
    model = Author
    ordering = ['pk']
    template_name = 'author_list.html'


class BookDetailView(APIView):
    """
    Вывод одной книги
    """
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)


class BooksListView(QueryAndSerializeMixin, generics.ListAPIView):
    """
    Вывох всех книг
    """


class BooksUpdateView(QueryAndSerializeMixin, UpdateAPIView):
    """
    Обновление данных из книги
    """


class BooksDeleteView(QueryAndSerializeMixin, DestroyAPIView):
    """
    Удаление книги
    """