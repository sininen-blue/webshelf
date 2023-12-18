from django.db import models


class Chapter(models.Model):
    title = models.TextField(max_length=256)
