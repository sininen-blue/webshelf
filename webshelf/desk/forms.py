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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "bg-blue-700"})
