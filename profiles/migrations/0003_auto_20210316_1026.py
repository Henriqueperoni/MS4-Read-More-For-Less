# Generated by Django 3.1.6 on 2021-03-16 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20210316_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_authors',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_books',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='genres',
        ),
        migrations.CreateModel(
            name='BookPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(blank=True, choices=[('business', 'Business'), ('children', 'Children'), ('mindset', 'Mindset'), ('romance', 'Romance'), ('horror', 'Horror'), ('crime', 'Crime'), ('biography', 'Biography')], max_length=20)),
                ('favorite_authors', models.TextField(blank=True, max_length=100)),
                ('favorite_books', models.TextField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
