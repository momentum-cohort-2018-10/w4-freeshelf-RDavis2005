# Generated by Django 2.1.3 on 2018-11-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0006_auto_20181120_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]