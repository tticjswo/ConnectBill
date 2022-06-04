# Generated by Django 4.0.5 on 2022-06-04 17:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquired_date', models.CharField(max_length=40)),
                ('certificate_name', models.CharField(max_length=40)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DesignerPopol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=300)),
            ],
            options={
                'verbose_name': 'Portfolio',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('small_image', models.ImageField(blank=True, upload_to=portfolio.models.path_and_rename_sumnail)),
                ('description', models.TextField()),
                ('participation_date', models.CharField(max_length=100)),
                ('client', models.CharField(blank=True, max_length=100, null=True)),
                ('score', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('portfolio', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.designerpopol')),
            ],
        ),
        migrations.CreateModel(
            name='EducationAndCareer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_period', models.CharField(max_length=40)),
                ('company_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.designerpopol')),
            ],
        ),
    ]
