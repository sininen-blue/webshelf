from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    synopsis = models.TextField(max_length=4096)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    chapter_number = models.IntegerField(unique=True)

    title = models.CharField(max_length=256)
    content = models.TextField()
