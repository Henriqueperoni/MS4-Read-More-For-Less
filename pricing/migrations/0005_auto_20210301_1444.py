# Generated by Django 3.1.6 on 2021-03-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0004_auto_20210228_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='introduction',
            field=models.TextField(default='Gonna fix all later', max_length=600),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pricing',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
