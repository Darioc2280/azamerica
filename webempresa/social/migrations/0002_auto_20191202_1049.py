# Generated by Django 2.0 on 2019-12-02 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
    ]
