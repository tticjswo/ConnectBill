# Generated by Django 4.0.5 on 2022-06-04 21:27

import django.core.validators
from django.db import migrations, models
import userReview.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('small_image', models.ImageField(upload_to=userReview.models.path_and_rename_sumnail)),
                ('panorama_image', models.ImageField(upload_to=userReview.models.path_and_rename_panorama_image)),
                ('description', models.TextField(null=True)),
                ('title', models.CharField(blank=True, default=None, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'customerReview',
            },
        ),
    ]
