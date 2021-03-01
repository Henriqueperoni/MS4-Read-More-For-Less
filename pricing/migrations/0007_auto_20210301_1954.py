# Generated by Django 3.1.6 on 2021-03-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0006_bookpreferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpreferences',
            name='favorite_authors',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bookpreferences',
            name='favorite_books',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bookpreferences',
            name='genres',
            field=models.CharField(blank=True, choices=[('romance', 'Romance'), ('children', 'Children'), ('business', 'Business'), ('horror', 'Horror'), ('mindset', 'Mindset'), ('crime', 'Crime'), ('biography', 'Biography')], max_length=20, null=True),
        ),
    ]
