from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    title_en = models.CharField(max_length=200, null=True)
    title_jp = models.CharField(max_length=200, null=True)
    previous_evolution = models.ForeignKey("self",
                                           on_delete=models.CASCADE,
                                           null=True, blank=True,
                                           related_name="next_evolution")

    def __str__(self):
        return str(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entity')
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()
