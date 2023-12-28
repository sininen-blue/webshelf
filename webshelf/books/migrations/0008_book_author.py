# Generated by Django 5.0 on 2023-12-22 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_created_date'),
        ('desk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='desk.authorprofile'),
            preserve_default=False,
        ),
    ]
