# Generated by Django 5.0.1 on 2024-01-11 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='images/thumbnails/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Превью поста'),
        ),
    ]