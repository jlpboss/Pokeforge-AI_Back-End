from fastapi import APIRouter, Depends
import requests
from pokeforge.utils.find_all_tiers import find_all_tiers
from pokeforge.schema.pokemonSchema import *
from pokeforge.utils.generate_new_pokemon import generate_new_pokemon

router = APIRouter()

api_url = "https://play.pokemonshowdown.com/data/pokedex.json"
response = requests.get(api_url)
if response.status_code == 200:
    response = response.json()
else:
    response = []

@router.get("/all-tiers")
def get_all_tiers():
    return find_all_tiers(response)

@router.post("/generate", response_model=PokemonOut)
def generate_pokemon(pokemon: PokemonIn):
    return generate_new_pokemon(pokemon, response)
