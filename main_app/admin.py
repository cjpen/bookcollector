from django.contrib import admin
from .models import Book, Bookmark, Genre

# Register your models here.
admin.site.register(Book)
admin.site.register(Bookmark)
admin.site.register(Genre)