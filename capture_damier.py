import cv2 as cv
import os

# Dimension du damier utilisé pour la calibration
DIM_DAMIER = (7, 7)

# Compteur d'images sauvegardées
compteur_images = 0  

# Chemin du dossier où seront stockées les images
dossier_images = "images"

# Vérifier si le dossier existe, sinon le créer
if not os.path.isdir(dossier_images):
    os.makedirs(dossier_images)
    print(f'Le dossier "{dossier_images}" a été créé.')
else:
    print(f'Le dossier "{dossier_images}" existe déjà.')

# Critères pour l'affinement des coins détectés
criteres_affinage = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Fonction pour détecter les coins du damier
def detecter_damier(image, image_gris, criteres, dim_damier):
    # Détection des coins du damier
    trouve, coins = cv.findChessboardCorners(image_gris, dim_damier)
    if trouve:
        # Affinement des coins pour plus de précision
        coins_affines = cv.cornerSubPix(image_gris, coins, (3, 3), (-1, -1), criteres)
        # Dessiner les coins détectés sur l'image
        image = cv.drawChessboardCorners(image, dim_damier, coins_affines, trouve)
    return image, trouve

# Initialisation de la webcam
camera = cv.VideoCapture(0)

while True:
    # Lecture de l'image depuis la webcam
    _, image = camera.read()
    copie_image = image.copy()  # copie pour sauvegarde
    # Conversion en niveaux de gris
    image_gris = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Détection du damier
    image_annotée, damier_detecte = detecter_damier(image, image_gris, criteres_affinage, DIM_DAMIER)

    # Affichage du nombre d'images sauvegardées
    cv.putText(image,f"Images sauvegardées : {compteur_images}",(30, 40),
               cv.FONT_HERSHEY_PLAIN,1.4,(0, 255, 0),2,cv.LINE_AA)

    # Affichage des fenêtres
    cv.imshow("Caméra", image)
    cv.imshow("Image originale", copie_image)

    # Lecture de la touche pressée
    touche = cv.waitKey(1)

    if touche == ord("q"):  # quitter avec 'q'
        break
    if touche == ord("s") and damier_detecte:  # sauvegarder avec 's' si damier détecté
        # Sauvegarde de l'image
        cv.imwrite(f"{dossier_images}/image{compteur_images}.png", copie_image)
        print(f"Image {compteur_images} sauvegardée.")
        compteur_images += 1  # incrémentation du compteur

# Libération de la caméra et fermeture des fenêtres
camera.release()
cv.destroyAllWindows()

print("Nombre total d'images sauvegardées :", compteur_images)
