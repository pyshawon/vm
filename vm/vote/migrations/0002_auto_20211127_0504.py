# Generated by Django 3.2.9 on 2021-11-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='area',
        ),
        migrations.AddField(
            model_name='vote',
            name='candidates',
            field=models.ManyToManyField(to='vote.Candidate'),
        ),
    ]
