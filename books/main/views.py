from django.shortcuts import render

from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import QueryAndSerializeMixin
from .models import Users, Books
from .serializers import BooksSerializer



class BookDetailView(APIView):
    """
    Вывод одной книги
    """
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)


class BooksListView(QueryAndSerializeMixin, ListAPIView):
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
