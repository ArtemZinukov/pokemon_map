# Generated by Django 2.2.24 on 2024-05-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]