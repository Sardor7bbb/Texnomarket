# Generated by Django 5.0.6 on 2024-06-15 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_image1_productmodel_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='image',
            new_name='image1',
        ),
    ]
