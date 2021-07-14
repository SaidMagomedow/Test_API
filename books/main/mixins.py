from .models import Books
from .serializers import BooksSerializer


class QueryAndSerializeMixin:

    queryset = Books.objects.all()
    serializer_class = BooksSerializer