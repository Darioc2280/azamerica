# Generated by Django 2.2.2 on 2019-12-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagesplay', '0006_remove_page_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='playground/pages/', verbose_name='imagen post'),
        ),
    ]