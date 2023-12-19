# Generated by Django 5.0 on 2023-12-19 12:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_chapter_chapter_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
