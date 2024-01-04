from django.contrib import admin
from .models import Book, Chapter, Review, Rating

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Review)
admin.site.register(Rating)
