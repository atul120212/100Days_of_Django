# Generated by Django 4.2.5 on 2023-09-19 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/ytubers/%Y/%m/')),
                ('video_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
                ('crew', models.CharField(max_length=255)),
                ('camera_type', models.CharField(max_length=255)),
                ('subs_count', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
