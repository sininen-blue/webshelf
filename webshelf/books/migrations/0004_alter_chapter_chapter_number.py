# Generated by Django 5.0 on 2023-12-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_chapter_chapter_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_number',
            field=models.IntegerField(blank=True),
        ),
    ]