import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
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


def get_photo_url(pokemon):
    return pokemon.pokemon.photo.url if pokemon.pokemon.photo else DEFAULT_IMAGE_URL


def show_all_pokemons(request):
    utc_time = timezone.now()
    query_time = timezone.localtime(utc_time)
    pokemons = PokemonEntity.objects.filter(appeared_at__lte=query_time,
                                            disappeared_at__gte=query_time)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        photo_url = get_photo_url(pokemon)
        full_url = request.build_absolute_uri(photo_url)
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            full_url
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        photo_url = pokemon.photo.url if pokemon.photo else DEFAULT_IMAGE_URL
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
    query_time = timezone.localtime(utc_time)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    requested_pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    requested_pokemon_entity = requested_pokemon.entities.filter(
            appeared_at__lte=query_time,
            disappeared_at__gte=query_time
        )

    for pokemon in requested_pokemon_entity:
        photo_url = get_photo_url(pokemon)
        full_url = request.build_absolute_uri(photo_url)
        add_pokemon(folium_map, pokemon.lat, pokemon.lon, full_url)
    pokemon = {
        "title_ru": requested_pokemon.title,
        "img_url": requested_pokemon.photo.url,
        "description": requested_pokemon.description,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
    }

    if requested_pokemon.previous_evolution:
        pokemon["previous_evolution"] = {
            "title_ru": requested_pokemon.previous_evolution.title,
            "pokemon_id": requested_pokemon.previous_evolution.pk,
            "img_url": requested_pokemon.previous_evolution.photo.url
        }

    next_evolution = requested_pokemon.next_evolutions.first()
    if next_evolution:
        pokemon["next_evolution"] = {
            "title_ru": next_evolution.title,
            "pokemon_id": next_evolution.pk,
            "img_url": next_evolution.photo.url
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
