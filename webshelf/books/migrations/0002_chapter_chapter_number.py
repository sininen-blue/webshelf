# Generated by Django 5.0 on 2023-12-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_number',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
