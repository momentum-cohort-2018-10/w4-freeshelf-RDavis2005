# Generated by Django 2.1.3 on 2018-11-19 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0003_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]