from django.urls import path

from .views import AuthorListView, BooksListView, BookDetailView, BooksUpdateView, BooksDeleteView

app_name = 'main'

urlpatterns = [
    path('', AuthorListView.as_view(), name='landing'),
    path('books/list/', BooksListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BooksUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BooksDeleteView.as_view(), name='book-delete'),

]