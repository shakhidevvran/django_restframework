# Generated by Django 4.1.1 on 2022-09-25 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_review_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
    ]