# Generated by Django 4.2.5 on 2023-09-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caughtpokemon',
            name='height',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
