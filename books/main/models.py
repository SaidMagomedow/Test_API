from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class UserMixin:
    def get_full_name(self):
        return ' '.join(filter(None, [self.last_name, self.first_name]))  # noqa

    def get_fio(self):
        return ' '.join(filter(None, [self.last_name, self.first_name, self.middle_name]))  # noqa

    def get_number(self):
        return self.pk


class Users(UserMixin, AbstractBaseUser):
    USER_TYPES = (
        (AUTHOR := 'AUTHOR', 'Автор'),
        (READER := 'READER', 'Читатель')
    )

    user_type = models.CharField('Тип пользователя', choices=USER_TYPES, default='READER', max_length=10)
    country = models.CharField('Страна', max_length=30)
    email = models.EmailField('email', unique=True)
    last_name = models.CharField('фамилия', max_length=150, blank=True)
    first_name = models.CharField('имя', max_length=30)
    middle_name = models.CharField('отчество', max_length=150, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name()


class Books(models.Model):
    author = models.ForeignKey(Users, models.DO_NOTHING, verbose_name='Автор')
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', max_length=255)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
