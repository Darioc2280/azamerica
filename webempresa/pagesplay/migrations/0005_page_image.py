# Generated by Django 2.2.2 on 2019-12-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagesplay', '0004_remove_page_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(default='default/default.jpg', upload_to='playground/pages/', verbose_name='imagen post'),
        ),
    ]
