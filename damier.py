import cv2
import numpy as np

# Fonction pour générer et enregistrer une mire en damier 8x8
def enregistrer_damier(nom_fichier, taille_carre_cm):
    nb_lignes, nb_colonnes = 8, 8  # dimensions du damier (8x8)
    pixels_par_cm = 100  # résolution d'impression (100 px par cm)

    # Conversion de la taille d'un carré en cm vers pixels
    taille_carre_px = int(taille_carre_cm * pixels_par_cm)

    # Création d'une image en niveaux de gris (noir = 0, blanc = 255)
    damier = np.zeros((nb_lignes * taille_carre_px, nb_colonnes * taille_carre_px), dtype=np.uint8)

    # Remplissage des cases blanches (lignes et colonnes paires)
    for ligne in range(0, nb_lignes, 2):
        for colonne in range(0, nb_colonnes, 2):
            damier[ligne * taille_carre_px : (ligne + 1) * taille_carre_px,
                   colonne * taille_carre_px : (colonne + 1) * taille_carre_px] = 255

    # Remplissage des cases blanches (lignes et colonnes impaires)
    for ligne in range(1, nb_lignes, 2):
        for colonne in range(1, nb_colonnes, 2):
            damier[ligne * taille_carre_px : (ligne + 1) * taille_carre_px,
                   colonne * taille_carre_px : (colonne + 1) * taille_carre_px] = 255

    # Sauvegarde de l'image au format PNG
    cv2.imwrite(nom_fichier, damier)
    print(f"Damier enregistré dans : {nom_fichier}")


# Exemple d’utilisation : création d’un damier avec des carrés de 2 cm
enregistrer_damier("damier_8x8.png", taille_carre_cm=2)

