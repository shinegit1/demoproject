# Generated by Django 4.1 on 2023-02-26 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='country',
        ),
    ]
