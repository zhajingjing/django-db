from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    # ex: /books/user/
    path("user/", views.user_list, name="user_list"),
    # ex: /books/user/query/
    path("user/query", views.user_query, name="user_query"),
    # ex: /books/user/create/
    path("user/create/", views.user_create, name="user_create"),
    # ex: /books/user/5/
    path("user/<int:user_id>/", views.user_detail, name="user_detail"),
    # ex: /books/user/5/update
    path("user/<int:user_id>/update", views.user_update, name="user_update"),
    # ex: /books/user/5/delete
    path("user/<int:user_id>/delete", views.user_delete, name="user_delete"),
    
    # ex: /books/book/
    path("book/", views.book_list, name="book_list"),
    # ex: /books/book/query/
    path("book/query", views.book_query, name="book_query"),
    # ex: /books/book/create/
    path("book/create/", views.book_create, name="book_create"),
    # ex: /books/book/1/
    path("book/<int:book_id>/", views.book_detail, name="book_detail"),
    # ex: /books/book/5/update
    path("book/<int:book_id>/update", views.book_update, name="book_update"),
    # ex: /books/user/5/delete
    path("book/<int:book_id>/book_delete", views.book_delete, name="book_delete"),
]
