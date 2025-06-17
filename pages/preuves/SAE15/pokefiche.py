import requests
from md_to_html import convert

def download_poke(id: int) -> dict :
    """
    Télécharge les données d'un Pokémon à partir de son identifiant via l'API REST de PokéAPI.
    """
    
    json_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/").json()
    return json_data


def poke_to_md(data: dict, filename: str) -> None :
    """
    Prend un dictionnaire représentant un Pokémon et un nom de fichier, et génère un fichier Markdown représentant toutes les informations sur le Pokémon.
    """
    
    id = data["id"]
    nom = data["name"]
    poids = data["weight"]
    taille = data["height"]
    types = []
    stats = []
   
    print(f"Extraction des données pour le Pokémon : {nom}")
   
    for element in data["types"]:
        types.append(element["type"]["name"])
        
    for element in data["stats"]:
        stats.append((element["stat"]["name"], element["base_stat"]))

    print(f"Création du fichier Markdown : {filename}")

    with open(filename, 'w') as md:
        md.write(f"# Données sur le Pokémon {nom}")
        md.write(f"\nID : {id}")
        md.write(f"\n")
        md.write(f"\nPoids : {poids}")
        md.write(f"\n")
        md.write(f"\nTaille : {taille}")
        md.write(f"\n## Types")
        for type_name in types:
            md.write(f"\n- {type_name}")
        md.write(f"\n## Stats")
        for stat_name, stat_value in stats:
            md.write(f"\n- {stat_name} : {stat_value}")
        md.write(f"\n## Image du Pokémon (sprite)")
        md.write(f"\n![Image du Pokémon {nom}](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png)")
            
    print(f"Fichier Markdown généré avec succès : {filename}")
        

def fiche_pokemon(id: int) -> None :
    """
    Génère une fiche Markdown et une fiche HTML sur un Pokéon à partir de son identifiant.
    """
    
    infos_pokemon = download_poke(id)
    poke_to_md(infos_pokemon,f"pokefiche_{id}.md")
    convert(f"pokefiche_{id}.md",f"pokefiche_{id}.html")
    
    print(f"Fichier Markdown converti en HTML avec succès : {f"pokefiche_{id}.html"}")
