# Generated by Django 3.0.9 on 2020-08-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socius', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorycreation',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
    ]
