# Generated by Django 2.2.24 on 2024-05-14 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20240514_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolution', to='pokemon_entities.Pokemon', verbose_name='из кого эволюционирует'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='имя покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='имя покемона на англ.'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='имя покемона на японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(null=True, verbose_name='появится в'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(verbose_name='защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(null=True, verbose_name='пропадет в'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(verbose_name='здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(verbose_name='уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity', to='pokemon_entities.Pokemon', verbose_name='имя покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(verbose_name='выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(verbose_name='сила'),
        ),
    ]
