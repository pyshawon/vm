# Generated by Django 3.2.9 on 2021-11-27 10:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0002_auto_20211127_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
