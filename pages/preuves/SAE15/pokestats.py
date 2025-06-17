import requests
from md_to_html import convert

def get_dataset() -> dict :
    """
    Télécharge les statistiques de vitesse moyenne des Pokémon pour chaque génération.
    """

    json_data = requests.get("https://pokeapi.co/api/v2/generation/").json() # Stocke la page de chaque générations

    dataset = {}

    for generation in json_data["results"] : # Boucle qui récupère l'URL de chaque Pokémon de chaque génération
        generation_name = generation["name"] # Stocke le nom de chaque génération à l'aide d'un dictionnaire
        generation_url = requests.get(generation["url"]).json() # Stocke l'URL de chaque génération
        pokemon_urls = []
        for pokemon in generation_url["pokemon_species"] : # Stocke les URLs de toutes les espèces de Pokémon de la génération actuelle
            pokemon_urls.append(pokemon["url"])

        total_speed = 0
        count = 0

        for url in pokemon_urls : # Boucle qui utilise l'URL de chaque Pokémon pour récupérer ses données
            pokemon_data = requests.get(url.replace("pokemon-species", "pokemon")).json() # Pour avoir une fiche plus complète
            speed_stat = None
            for stat in pokemon_data["stats"]: # Parcourt chaque élément de la liste
                if stat["stat"]["name"] == "speed": # Vérifie le nom de la statistique
                    speed_stat = stat["base_stat"] # Récupère la valeur de la vitesse
                    break # Sort de la boucle dès qu'on a trouvé la statistique de vitesse
            
            total_speed += speed_stat # Addition de toutes les vitesse
            count += 1 # Nombre de stats de vitesses

        
        dataset[generation_name] = total_speed / count # Calcule et stocke la vitesse moyenne des Pokémons pour chaque génération indépendament

    return dataset


def compute_statistics(dataset: dict) -> dict :
    """
    Calcule les statistiques sur les vitesses des Pokémons par génération.
    """
    statistics = {
        "max_speed": max(dataset.values()), # Génération ayant la plus faible vitesse moyenne
        "min_speed": min(dataset.values()), # Génération ayant la plus grande vitesse moyenne
        "average_speed": sum(dataset.values()) / len(dataset) # Moyenne pour chaques générations
    }
    return statistics


def dataset_to_md(dataset: dict, filename: str) -> None :
    """
    Génère un fichier Markdown présentant les vitesses moyennes des Pokémon par génération.
    """
    with open(filename, 'w') as md_file:
        md_file.write("# Statistiques des vitesses moyennes des Pokémon\n\n")

        for generation, speed in dataset.items() :
            md_file.write(f"## {generation}\n")
            md_file.write(f"- Vitesse moyenne : {speed:.2f}\n\n")

        stats = compute_statistics(dataset)
        md_file.write("# Statistiques globales\n\n")
        md_file.write(f"- Vitesse maximale : {stats['max_speed']:.2f}\n")
        md_file.write(f"- Vitesse minimale : {stats['min_speed']:.2f}\n")
        md_file.write(f"- Vitesse moyenne globale : {stats['average_speed']:.2f}\n")


def infos_locales() -> None :
    """
    Fonction principale qui exécute les fonction ci dessus.
    """
    print("Téléchargement des données en cours")
    dataset_to_md(get_dataset(), "pokestats.md")
    print(f"Fichier Markdown converti en HTML avec succès : pokestats.md")

    convert("pokestats.md", "pokestats.html")
    print(f"Fichier Markdown converti en HTML avec succès : pokestats.html")