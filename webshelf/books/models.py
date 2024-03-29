from django.db import models
from desk.models import AuthorProfile


class Book(models.Model):
    author = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE)

    # TODO have a file name function
    cover = models.ImageField(
        upload_to="covers/",
        height_field="cover_h",
        width_field="cover_w",
        default="covers/cover_default.jpg",
    )
    cover_w = models.IntegerField(default=0)
    cover_h = models.IntegerField(default=0)

    title = models.CharField(max_length=256)
    synopsis = models.TextField(max_length=4096)

    created_date = models.DateTimeField(auto_now_add=True)

    # these should have values between 0 and 100
    quality_rating = models.IntegerField(default=0)
    popularity_rating = models.IntegerField(default=0)

    words = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    follows = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapters")

    chapter_number = models.IntegerField()

    created_date = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=256)
    content = models.TextField()


class Review(models.Model):
    author = models.ForeignKey(
        AuthorProfile, on_delete=models.CASCADE, related_name="reviews"
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")

    title = models.CharField(max_length=256)
    content = models.CharField(max_length=4096)


class Rating(models.Model):
    author = models.ForeignKey(
        AuthorProfile, on_delete=models.CASCADE, related_name="ratings"
    )
    quality_choice = {
        "Poorly": "poorly",
        "Well": "well",
    }
    quality_rating = models.CharField(max_length=8, choices=quality_choice)
    popularity_rating = models.IntegerField(default=0)
