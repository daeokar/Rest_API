# Generated by Django 2.2 on 2021-04-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_collge'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.SmallIntegerField(default=0),
        ),
    ]
