from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.db.models import Q
from .forms import BookForm, UserForm
from .models import Book, User


def book_list(request):
    """Show the book list."""
    books = Book.objects.all()
    context = {
        "books": books,
        "query_condition": {"q_field": "book_name", "q_filter": "startswith", "q_value": ""}
    }
    return render(request, "books/book_list.html", context)


def book_detail(request, book_id):
    """Show the detail page of books."""
    book = get_object_or_404(Book, pk=book_id)
    context = {"book": book}
    return render(request, "books/book_detail.html", context)


def book_query(request):
    """Show the result of the query."""
    q_field = request.GET.get('q_field') 
    # field: book_name, price
    q_filter = request.GET.get('q_filter') 
    # filter: book_name: startswith, endswith, contains
    # filter: price: lte, gte, between (use "," to split)
    q_value = request.GET.get('q_value')

    books = {}

    if q_field == 'book_name':
        if q_filter == 'startswith':
            books = Book.objects.filter(book_name__startswith=q_value)
        elif q_filter == 'endswith':
            books = Book.objects.filter(book_name__endswith=q_value)
        elif q_filter == 'contains':
            books = Book.objects.filter(book_name__contains=q_value)
        else:
            books = Book.objects.all()
    elif q_field == 'price':
        if q_filter == 'lte':
            x = float(q_value)
            books = Book.objects.filter(price__lte=x)
        elif q_filter == 'gte':
            y = float(q_value)
            books = Book.objects.filter(price__gte=y)
        elif q_filter == 'between':
            val = q_value.split(",")
            y = val[0]
            x = val[1]
            books = Book.objects.filter(Q(price__lte=x) & Q(price__gte=y))
        else:
            books = Book.objects.all()

    context = {
        "books": books,
        "query_condition": {"q_field": q_field, "q_filter": q_filter, "q_value": q_value}
    }

    return render(request, "books/book_list.html", context)


def book_create(request):
    """Create a book in the database."""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:book_list')) 
            # book_list is the name of the url pattern that maps to '/books/book/'
            # reverse() generates the url dynamically
    form = BookForm()
    context = {"form": form}
    return render(request, "books/book_form.html", context)


def book_update(request, book_id):
    """Update the book_id."""
    book_obj = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(instance=book_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:book_detail', args=[book_id]))
    form = BookForm(instance=book_obj)
    context = {
        "form": form,
        "object": book_obj
    }
    return render(request, "books/book_form.html", context)


def book_delete(request, book_id):
    """Delete the book."""
    book_obj = get_object_or_404(Book, pk=book_id)
    book_obj.delete()
    return HttpResponseRedirect(reverse("books:book_list"))


def user_list(request):
    """Show the user list."""
    users = User.objects.all()
    context = {
        "users": users,
        "query_condition": {"q_field": "user_name", "q_filter": "startswith", "q_value": ""}
    }
    return render(request, "books/user_list.html", context)


def user_detail(request, user_id):
    """Show the detail page of user."""
    user = get_object_or_404(User, pk=user_id)
    context = {"user": user}
    return render(request, "books/user_detail.html", context)


def user_create(request):
    """Create a user in the database."""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:user_list')) 
    form = UserForm()
    context = {"form": form}
    return render(request, "books/user_form.html", context)


def user_delete(request, user_id):
    """Delete the user."""
    user_obj = get_object_or_404(User, pk=user_id)
    user_obj.delete()
    return HttpResponseRedirect(reverse("books:user_list"))


def user_query(request):
    """Show the result of the query."""
    q_field = request.GET.get('q_field') 
    # field: user_name, age
    q_filter = request.GET.get('q_filter') 
    # filter: user_name: startswith, endswith, contains
    # filter: age: lte, gte, between (use "," to split)
    q_value = request.GET.get('q_value')

    users = {}

    if q_field == 'user_name':
        if q_filter == 'startswith':
            users = User.objects.filter(user_name__startswith=q_value)
        elif q_filter == 'endswith':
            users = User.objects.filter(user_name__endswith=q_value)
        elif q_filter == 'contains':
            users = User.objects.filter(user_name__contains=q_value)
        else:
            users = User.objects.all()
    elif q_field == 'age':
        if q_filter == 'lte':
            x = float(q_value)
            users = User.objects.filter(age__lte=x)
        elif q_filter == 'gte':
            y = float(q_value)
            users = User.objects.filter(age__gte=y)
        elif q_filter == 'between':
            val = q_value.split(",")
            y = val[0]
            x = val[1]
            users = User.objects.filter(Q(age__lte=x) & Q(age__gte=y))
        else:
            users = User.objects.all()

    context = {
        "users": users,
        "query_condition": {"q_field": q_field, "q_filter": q_filter, "q_value": q_value}
    }

    return render(request, "books/user_list.html", context)


def user_update(request, user_id):
    """Update the user_id."""
    user_obj = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(instance=user_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:user_detail', args=[user_id]))
    form = UserForm(instance=user_obj)
    context = {
        "form": form,
        "object": user_obj
    }
    return render(request, "books/user_form.html", context)