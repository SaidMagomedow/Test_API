from django.urls import path

from .views import AuthorListView

app_name = 'main'

urlpatterns = [
    path('', AuthorListView.as_view(), name='landing')
]