# Generated by Django 4.0 on 2021-12-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0006_alter_ticket_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
