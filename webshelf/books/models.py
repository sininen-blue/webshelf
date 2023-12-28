from django.db import models
from desk.models import AuthorProfile


class Book(models.Model):
    author = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE)

    title = models.CharField(max_length=256)
    synopsis = models.TextField(max_length=4096)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    chapter_number = models.IntegerField()

    title = models.CharField(max_length=256)
    content = models.TextField()
