# Generated by Django 4.0.6 on 2022-07-05 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(to='movies.actor'),
        ),
    ]
