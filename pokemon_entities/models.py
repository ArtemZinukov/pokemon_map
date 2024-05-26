from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="имя покемона")
    photo = models.ImageField(null=True, blank=True, verbose_name="фото")
    description = models.TextField(null=True, blank=True, verbose_name="описание")
    title_en = models.CharField(max_length=200, null=True, blank=True, verbose_name="имя покемона на англ.")
    title_jp = models.CharField(max_length=200, null=True, blank=True, verbose_name="имя покемона на японском")
    previous_evolution = models.ForeignKey("self",
                                           verbose_name="из кого эволюционирует",
                                           on_delete=models.CASCADE,
                                           null=True, blank=True,
                                           related_name="next_evolutions")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities', verbose_name="имя покемона")
    lat = models.FloatField(verbose_name="широта")
    lon = models.FloatField(verbose_name="долгота")
    appeared_at = models.DateTimeField(null=True, verbose_name="появится в")
    disappeared_at = models.DateTimeField(null=True, verbose_name="пропадет в")
    level = models.IntegerField(verbose_name="уровень")
    health = models.IntegerField(verbose_name="здоровье")
    strength = models.IntegerField(verbose_name="сила")
    defence = models.IntegerField(verbose_name="защита")
    stamina = models.IntegerField(verbose_name="выносливость")
