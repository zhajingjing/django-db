from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.book_name


class User(models.Model):
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()
    liked_books = models.ManyToManyField(Book)

    def __str__(self):
        return self.user_name

