# Generated by Django 2.2.24 on 2024-05-14 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20240514_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title_ru',
            new_name='title',
        ),
    ]
