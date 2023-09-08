import requests
from django.shortcuts import render

def index(request):
    response = requests.get('https://pokeapi.co/api/v2/type/')
    data = response.json()
    return render(request, 'pokedex_types.html', {'data': data})

from django.shortcuts import render
import requests

def search(request):
    pokename = request.GET.get('Poketype', '')

    # Dictionary mapping type names to numeric IDs
    poketype_dict = {
        'normal': 1,
        'fighting': 2,
        'flying': 3,
        'poison': 4,
        'ground': 5,
        'rock': 6,
        'bug': 7,
        'ghost': 8,
        'steel': 9,
        'fire': 10,
        'water': 11,
        'grass': 12,
        'electric': 13,
        'psychic': 14,
        'ice': 15,
        'dragon': 16,
        'dark': 17,
        'fairy': 18,
        'unknown': 10001,
        'shadow': 10002,
    }

    poke_number = poketype_dict.get(pokename, '')

    if poke_number:
        response2 = requests.get(f'https://pokeapi.co/api/v2/type/{poke_number}/')
        data2 = response2.json()
    return render(request, 'pokedex_search.html', {'data2': data2, 'pokename': pokename})


