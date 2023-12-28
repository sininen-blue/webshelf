from django.forms import ModelForm
from books.models import Book, Chapter


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "synopsis"]


class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = ["title", "content"]
