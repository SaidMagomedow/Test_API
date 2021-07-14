from rest_framework import serializers

from .models import Books


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('pk', 'title', 'description', 'author')


class BooksDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'

