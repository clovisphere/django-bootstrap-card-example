from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.order_by('id')
    # -- transform data before using it --
    data = books.values()
    # let's do something fancy -- this should be changed
    context = {
        'tags': [
            {'name': 'Programming', 'books': data[:2]},
            {'name': 'Programming', 'books': data[2:4]},
            {'name': 'Programming', 'books': data[4:]},
        ]
    }
    return render(request, 'books/index.html', context)