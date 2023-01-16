from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book


def index(request):
    return HttpResponse("Hello World!")

# showing the book details in the url
def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book': book})
