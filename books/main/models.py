from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField('Имя', max_length=255)
    country = models.CharField('Страна', max_length=30)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Books(models.Model):
    author = models.ForeignKey(Author, models.DO_NOTHING, verbose_name='Автор')
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', max_length=255)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
