# Generated by Django 4.0 on 2021-12-20 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0004_alter_review_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='note',
        ),
    ]
