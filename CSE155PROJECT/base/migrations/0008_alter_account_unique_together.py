# Generated by Django 4.1.7 on 2023-03-24 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_image_multipleimage_images'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('profile', 'username')},
        ),
    ]