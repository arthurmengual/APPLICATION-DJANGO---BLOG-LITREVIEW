# Generated by Django 4.0 on 2021-12-12 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollows',
            name='follower',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='authentication.user'),
        ),
        migrations.AlterField(
            model_name='userfollows',
            name='following',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='authentication.user'),
        ),
    ]
