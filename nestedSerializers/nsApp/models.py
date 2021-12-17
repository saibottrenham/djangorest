from django.db import models


# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    ratings = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.title
