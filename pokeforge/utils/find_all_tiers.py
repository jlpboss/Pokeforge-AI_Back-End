import requests
def find_all_tiers(all_pokemon: dict):
    all_tiers = []
    for pokemon in all_pokemon:
        try:
            if all_pokemon[pokemon]['tier'] not in all_tiers:
                all_tiers.append(all_pokemon[pokemon]['tier'])
        except:
            pass
    return all_tiers

if __name__ == "__main__":
    api_url = "https://play.pokemonshowdown.com/data/pokedex.json"
    response = requests.get(api_url)
    if response.status_code == 200:
        response = response.json()
    else:
        response = []
    print(find_all_tiers(response))