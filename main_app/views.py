from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookmarkForm

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
    return render(request, 'books/detail.html', { 
        'book': book, 
        'bookmark_form': bookmark_form 
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