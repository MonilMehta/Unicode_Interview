import requests
from django.shortcuts import redirect, render
from .models import CaughtPokemon
import requests

def index(request):
    api_url = 'https://pokeapi.co/api/v2/type/' 
    response = requests.get(api_url)
    data = response.json()
    return render(request, 'pokedex_types.html', {'data': data})

def search(request):
    pokename = request.GET.get('Poketype', '')
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

    response2 = requests.get(f'https://pokeapi.co/api/v2/type/{poke_number}/')
    data2 = response2.json()
    return render(request, 'pokedex_search.html', {'data2': data2, 'pokename': pokename})

def caught(request):
    if request.method == 'POST':
        name = request.POST.get('pokemon_name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}/'
        response = requests.get(url)
        data3=response.json()
        height = data3.get('height',0)
        if CaughtPokemon.objects.filter(name=name).exists():
            pokemon = CaughtPokemon.objects.get(name=name)
            pokemon.level += 1
            pokemon.height = height
            pokemon.save()
        else:
            CaughtPokemon.objects.create(name=name, level=1)

    return render(request,'caught.html')

def list(request):
    caught_pokemon = CaughtPokemon.objects.all()
    return render(request, 'list.html', {'caught_pokemon': caught_pokemon})

