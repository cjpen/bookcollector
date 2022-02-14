from django.forms import ModelForm
from .models import Bookmark, Genre

class BookmarkForm(ModelForm):
  class Meta:
    model = Bookmark
    fields = ['date', 'page']

class GenreForm(ModelForm):
  class Meta:
    model = Genre
    fields = '__all__'