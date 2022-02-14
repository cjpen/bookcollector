from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name = models.CharField('Name of Genre', max_length=50)

    def get_absolute_url(self):
        return reverse('genre_list')

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_date = models.CharField(max_length=4)
    isbn = models.CharField(max_length=13)

    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Bookmark(models.Model):
    date = models.DateField('Log Date')
    page = models.CharField('Page stopped on', max_length=5)

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Read until {self.page} on {self.date}"

    class Meta:
        ordering = ['-page']


