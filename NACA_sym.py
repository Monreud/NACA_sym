"""
Auteur : Augustin Montredon
Ce script permet d'afficher des profils NACA symétriques (à 4 chiffres) avec matplolib et la fonction pyplot
L'utilisateur doit entrer :
- les 4 chiffres du profil (commençant par '00')
- La corde du profil
- Le nombre de points souhaité pour le tracé
- Le type de la distribution
Le script calcule également l'épaisseur maximale du profil et sa position.
"""

import numpy as np
import matplotlib.pyplot as plt


def points_tables():

    # Entrées utilisateur
    profil = str(input('Veuillez entrer les 4 chiffres du profil NACA symétrique : '))

    while 1:
        if len(profil) != 4:
            profil = str(input('Veuillez entrer les 4 chiffres du profil NACA symétrique : '))
        else:
            break
    t = int(profil[2:]) / 100
    corde = int(input('Veuillez entrer la corde du profil en mètres : '))
    nb_points = int(input('Veuillez entrer le nombre de points le long de la corde : '))
    distribution = int(input('Quel est le type de distribution souhaitée, linéaire ou non-uniforme ? '
                             'Entrez 1 ou 2 : '))

    # Création du tableaux numpy x_up selon le type de distribution
    if distribution == 1:
        nom_distrib = 'linéaire'
        xc = np.linspace(0, 1, nb_points)
        x_up = xc.copy() * corde

    else:
        nom_distrib = 'non-uniforme'
        theta = np.linspace(0, np.pi, nb_points)
        xc = 0.5 * (1 - np.cos(theta))
        x_up = xc.copy() * corde

    # Création des variables restantes yt, x_down, y_up et y_down
    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.126 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    x_down = x_up.copy()
    y_up = yt * corde
    y_down = -y_up.copy()

    # Calcul de la position de l'épaisseur maximal
    pos_epaisseur_max = np.argmax(y_up)
    x_epais_max = float(x_up[pos_epaisseur_max])
    y_epais_max = float(y_up[pos_epaisseur_max])

    print('L épaisseur maximale se trouve à x = ', x_up[pos_epaisseur_max], 'm')
    print('l épaisseur max est ', 2 * y_up[pos_epaisseur_max], 'm')


    # Création des courbes et de l'épaisseur maximale
    plt.plot(x_up, y_up, label='Extrados')
    plt.plot(x_down, y_down, label='Intrados')
    plt.plot(x_up[pos_epaisseur_max], y_up[pos_epaisseur_max], 'ro')

    # Annotation, label et titre
    plt.annotate('Épaisseur maximale du profil', (x_epais_max, y_epais_max))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Profil NACA00{t*100} - Distribution {nom_distrib}')

    # Mise à l'échelle de la courbe
    plt.axis('equal')
    plt.ylim(-0.2*corde, 0.2*corde)
    plt.grid(True)
    plt.legend()

    # Affichage des courbes
    plt.show()


if __name__ == '__main__':
    points_tables()
