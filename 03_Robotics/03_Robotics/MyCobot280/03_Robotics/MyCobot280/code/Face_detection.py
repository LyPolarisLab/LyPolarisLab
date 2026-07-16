import cv2
import os

#Trouve le dossier où se situe le fichier haarcascade
dossier = os.path.dirname(os.path.abspath(__file__))

#Charger le detecteur de visages (fourni avec OpenCv)
detecteur = cv2.CascadeClassifier(os.path.join(dossier, "haarcascade_frontalface_default.xml"))

camera =cv2.VideoCapture(0)

while True:
    ret, image = camera.read()

    #Convertir en noir et blanc (le detecteur travaille comme cela)
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Detecter les visages -> renvoie une liste de positions 
    visages = detecteur.detectMultiScale(gris, 1.3, 5)

    #Dessiner un rectangle autour de chaque visage
    for (x, y, largeur, hauteur) in visages:
        cv2.rectangle(image, (x, y), (x + largeur, y + hauteur), (0, 255, 0), 3)

    cv2.imshow("Detection de visage", image)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()




