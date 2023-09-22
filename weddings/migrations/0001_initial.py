# Generated by Django 4.2.5 on 2023-09-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeddingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('event_type', models.CharField(max_length=255)),
                ('photographer_name', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
