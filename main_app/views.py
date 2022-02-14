from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Book, Genre
from .forms import BookmarkForm, GenreForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', { 'books': books })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    bookmark_form = BookmarkForm()

    genre_ids = book.genres.all().values_list('id')
    genres = Genre.objects.exclude(id__in=genre_ids)

    return render(request, 'books/detail.html', {
        'book': book,
        'bookmark_form': bookmark_form,
        'genres': genres,
    })

def add_bookmark(request, book_id):
    form = BookmarkForm(request.POST)
    if form.is_valid():
        new_bookmark = form.save(commit=False)
        new_bookmark.book_id = book_id
        new_bookmark.save()
    return redirect('detail', book_id=book_id)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

class GenreList(ListView):
    model = Genre
    
class GenreCreate(CreateView):
    model = Genre
    fields = ['name']

def assoc_genre(request, book_id, genre_id):
  book = Book.objects.get(id=book_id)
  book.genres.add(genre_id)
  return redirect('detail', book_id=book_id)

def unassoc_genre(request, book_id, genre_id):
  book = Book.objects.get(id=book_id)
  book.genres.remove(genre_id)
  return redirect('detail', book_id=book_id)
