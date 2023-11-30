from fastapi import APIRouter, Depends
import requests
from pokeforge.utils.find_all_tiers import find_all_tiers

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