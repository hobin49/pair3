# Generated by Django 3.2.13 on 2022-10-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_review_movie_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.CharField(default=None, max_length=100),
        ),
    ]