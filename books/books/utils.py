from books.main.models import Users


def get_authors():
    return Users.objects.get(user_type=Users.AUTHOR)
