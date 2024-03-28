from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path('', views.show_index, name='index'),
]