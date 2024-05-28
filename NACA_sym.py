"""

"""

import numpy as np
import matplotlib.pyplot as plt


def points_tables():

    profil = str(input('Veuillez entrer les 4 chiffres du profil NACA symétrique : '))
    t = int(profil[2:]) / 100
    corde = float(input('Veuillez entrer la corde du profil en mètres : '))
    nb_points = int(input('Veuillez entrer le nombre de points le long de la corde : '))
    distribution = int(input('Quel est le type de distribution souhaitée, linéaire ou non-uniforme ? '
                             'Entrez 1 ou 2 : '))



    if distribution == 1:
        nom_distrib = 'linéaire'
        xc = np.linspace(0, 1, nb_points)
        x_up = xc.copy() * corde
        print(x_up)

    else:
        nom_distrib = 'non-uniforme'
        theta = np.linspace(0, np.pi, nb_points)
        xc = 0.5 * (1 - np.cos(theta))
        x_up = xc.copy() * corde
        print(x_up)

    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.126 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    x_down = x_up.copy()
    y_up = yt * corde
    y_down = -y_up.copy()

    pos_epaisseur_max = np.argmax(y_up)
    print('L épaisseur maximale se trouve à x = ', x_up[pos_epaisseur_max], 'm')
    print('l épaisseur max est ', 2 * y_up[pos_epaisseur_max], 'm')

    plt.plot(x_up, y_up, label='Extrados')
    plt.plot(x_down,y_down, label='Intrados')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Profil NACA00{t*100} - Distribution {nom_distrib}')
    plt.axis('equal')
    plt.ylim(-0.2*corde, 0.2*corde)
    plt.grid(True)
    plt.show()




if __name__ == '__main__':
    points_tables()
