# Generated by Django 3.1.6 on 2021-03-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_reason', models.CharField(choices=[('general_query', 'General Query'), ('technical_issue', 'Technical Issue'), ('plan_query', 'Plan Query'), ('delivery', 'Delivery')], default='general_query', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('comments', models.TextField(max_length=50)),
            ],
        ),
    ]
