# Generated by Django 4.2.5 on 2023-09-21 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0003_folder_folder_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weddingimage',
            name='photographer_name',
        ),
        migrations.RemoveField(
            model_name='weddingimage',
            name='title',
        ),
    ]
