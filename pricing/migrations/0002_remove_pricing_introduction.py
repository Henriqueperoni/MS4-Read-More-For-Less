# Generated by Django 3.1.6 on 2021-03-17 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='introduction',
        ),
    ]