# Generated by Django 4.0 on 2021-12-17 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='titleR',
        ),
    ]