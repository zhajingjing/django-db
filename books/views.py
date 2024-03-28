from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F

from .models import Book, User

def show_index(request):
    books = Book.objects.all()
    users = User.objects.all()
    context = {'books': books, 'users': users}
    return render(request, 'books/index.html', context)






