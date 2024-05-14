import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone


from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    utc_time = timezone.now()
    pokemons = PokemonEntity.objects.filter(appeared_at__lte=timezone.localtime(utc_time),
                                            disappeared_at__gte=timezone.localtime(utc_time))
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        photo_url = pokemon.pokemon.photo.url if pokemon.pokemon.photo else ""
        full_url = request.build_absolute_uri(photo_url)
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            full_url
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        photo_url = pokemon.photo.url if pokemon.photo else ""
        pokemons_on_page.append({
            'pokemon_id': pokemon.pk,
            'img_url': photo_url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    utc_time = timezone.now()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    requested_pokemon = Pokemon.objects.get(pk=pokemon_id)
    requested_pokemon_entity = list(
        requested_pokemon.entity.filter(
            appeared_at__lte=timezone.localtime(utc_time),
            disappeared_at__gte=timezone.localtime(utc_time)
        )
    )

    for pokemon in requested_pokemon_entity:
        photo_url = pokemon.pokemon.photo.url if pokemon.pokemon.photo else ""
        full_url = request.build_absolute_uri(photo_url)
        add_pokemon(folium_map, pokemon.lat, pokemon.lon, full_url)
    pokemon = {
        "title_ru": requested_pokemon.title,
        "img_url": requested_pokemon.photo.url,
        "description": requested_pokemon.description
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
