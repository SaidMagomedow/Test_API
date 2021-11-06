from test_plus import TestCase

from books.books.utils import get_authors


class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = get_authors()

    def setUp(self):
        self.path = self.reverse('main:author_list')

    def test_get(self):
        self.get_check_200(self.path)



