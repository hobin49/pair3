# Generated by Django 3.2.13 on 2022-10-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_review_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie_name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
