# Generated by Django 3.1.6 on 2021-03-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0011_auto_20210304_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookpreferences',
            old_name='favorite_authors',
            new_name='default_favorite_authors',
        ),
        migrations.RenameField(
            model_name='bookpreferences',
            old_name='favorite_books',
            new_name='default_favorite_books',
        ),
        migrations.RemoveField(
            model_name='bookpreferences',
            name='genres',
        ),
        migrations.AddField(
            model_name='bookpreferences',
            name='default_genres',
            field=models.CharField(blank=True, choices=[('mindset', 'Mindset'), ('horror', 'Horror'), ('children', 'Children'), ('business', 'Business'), ('biography', 'Biography'), ('crime', 'Crime'), ('romance', 'Romance')], max_length=20, null=True),
        ),
    ]
