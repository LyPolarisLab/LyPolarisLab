from pymycobot import MyCobot280
import time

#Toujours connexion au port COM3
mc= MyCobot280('COM3', 115200)
time.sleep(2)

continuer = True
liste_joints = [0, 0, 0, 0, 0, 0] # Liste pour stocker les angles des joints

while continuer:
    joint =int(input("Quel joint bouger? "))

    if joint == 0:
        print("Au revoir!")
        continuer = False
    elif joint <1 or joint >6:
        print("Joint invalide !")
    else:
        degres = int(input("De combien de degrés ? "))
        if degres > 140 or degres < -140:
            print("Limite atteinte !")
        else:
            liste_joints[joint - 1]= degres # Mettre à jour l'angle du joint sélectionné
            mc.send_angles(liste_joints, 30) # Envoyer les angles mis à jour au robot



