import requests
def find_pokemon_in_tier(tier: str, all_pokemon: dict):
    out = {}
    for pokemon in all_pokemon:
        try:
            if all_pokemon[pokemon]['tier'] == tier:
                out[pokemon] = all_pokemon[pokemon]
        except:
            pass
    return out

if __name__ == "__main__":
    api_url = "https://play.pokemonshowdown.com/data/pokedex.json"
    response = requests.get(api_url)
    if response.status_code == 200:
        response = response.json()
    else:
        response = []
    print(find_pokemon_in_tier("UU", response))