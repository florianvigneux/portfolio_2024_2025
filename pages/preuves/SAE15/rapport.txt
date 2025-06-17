## SAÉ 1.05 — Traiter des données
### Groupe : Godet Thomas, Vigneux Florian

# Choix techniques pertinents effectués sur la partie "statistiques de base"
Nous voulons étudier l'évolution des statistiques de vitesse moyenne des Pokémon à travers les générations dans l'objectif de savoir si Pokémon sont-ils devenus plus rapides avec le temps ? (la réponse est : pas spécifiquement)

Dans la fonction "get_dataset", au lieu de faire une ligne dédiée à chaque génération, nous avons préféré faire une boucle qui parcourt toutes les générations pour optimiser le code mais surtout pour que le code soit prêt pour les prichaines générations de Pokémons.

# Difficultés rencontrées et solutions trouvées
Utilisation dans la fonction "dataset_to_md" nous avons utilisé ".2f" pour que les nombres décimaux / à virgule flottante soient affichés avec 2 chiffres après la virgule.

# Ce que nous pensons avoir appris durant ce projet
Nous pensons avoir appris un certain nombre de méthodes d'optention et analyse de bases de données. C'était un bon moyen de découvrir le principe d'API qui est utilisé très fréquement.

# État d’avancement du projet
Les traductions en français ne sont malheureusement pas effectuées.

Le fichier pokestats.py fonctionnait parfaitement et renvoyait un html complet et sans aucune raison, de notre côté, maintenant quand on recharge le script il charge pendant beaucoup plus de temps que prévu (environ 1 miniute de base) et maintenant on dirait que ça ne finit pas de charger.