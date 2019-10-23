from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.order_by('id')
    # -- transform data before using it --
    data = books.values()
    # let's do something fancy -- this should be changed, we'd be able to have 2-3 books on each card.
    context = {
        'tags': [
            {'name': 'Programming', 'books': data},
            {'name': 'Programming', 'books': data},
            {'name': 'Programming', 'books': data},
        ]
    }
    return render(request, 'books/index.html', context)
