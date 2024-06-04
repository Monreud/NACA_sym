# Génération et tracé de profil NACA 4 chiffres symétrique
## Contenu du repo
- Le script du devoir 
- Ce fichier README.md
## Utilisation du script
Au lancement du script, on demande à l'utilisateur de saisir 4 informations :
- Les 4 chiffres du profil NACA symétriques (donc doit commencer par '00')
- La corde (traitée en mètres) du profil
- Le nombre de points souhaité pour le tracé
- Le type de distribution (linéaire ou non-uniforme) du profil

Selon la distribution choisie, le script va calculer différents tableaux pour x_up, y_up, x_down, y_down, xc et yt. La position de l'épaisseur maximale est ensuite calculée. 
Une fois tous les calculs réalisés, le script procède à l'affichage des courbes et renvoit dans la console la valeur et la position selon la corde de l'épaisseur maximale.
