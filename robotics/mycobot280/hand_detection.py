from pymycobot import MyCobot280
import time
import cv2
import mediapipe as mp
import threading



# Le detecteur de mains de MediaPipe
mp_mains = mp.solutions.hands
detecteur = mp_mains.Hands(max_num_hands=1) # Détecteur de main, pour le moment il est régler que sur une main
dessinateur = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0) # Initialisation

mc = MyCobot280('COM3',115200)

# Ajout des fonctionq

def position_repos():
    mc.send_angles([0, 0, 0, 0, 0, 0], 30)
    time.sleep(3)


def dire_bonjour(repetitions, vitesse):
    mc.send_angles([0, -30, -30,0 ,0 , 0], 30)
    time.sleep(3)
    for i in range(repetitions):
        mc.send_angles([-90, 2, 4, 40, 0, 0], vitesse)
        time.sleep(60/vitesse)
        mc.send_angles([-90, 2, 4, -40, 0, 0], vitesse)
        time.sleep(60/vitesse)




def non_non(repetitions, vitesse):
    mc.send_angles([0, -30, -30, 0, 0, 0], 30)
    time.sleep(3)
    for i in range(repetitions):
        mc.send_angles([-90, 2, 4, -20, 70,0], vitesse)
        time.sleep(60/vitesse)
        mc.send_angles([-90, 2, 4, -20, -70, 0], vitesse)
        time.sleep(60/vitesse)



def oui_oui(repetitions, vitesse):
    mc.send_angles([0, -30, -30, 0, 0, 0], 30)
    time.sleep(3)
    for i in range(repetitions):
        mc.send_angles([-120, -95, 100, 20, 40, 0], vitesse)
        time.sleep(60/vitesse)
        mc.send_angles([-120, -95, -100, 20, 40, 0], vitesse)
        time.sleep(60/vitesse)
    position_repos()




# Création de la variable-mémoire

geste_precedent = ""


#Sytème de boucle
while True:
    ret, image = camera.read() # Acquisition
    if not ret:  #Sytème de protection ligne 14 et 15
        continue  

    # MediaPipe travaille en RGB (OpenCV est en BGR)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Pré-traitement
    resultats = detecteur.process(image_rgb) # Affiche le résultat

    # S'il y a une main detectee, dessiner ses 21 points
    if resultats.multi_hand_landmarks:
     for main in resultats.multi_hand_landmarks:

        dessinateur.draw_landmarks(
            image,
            main,
            mp_mains.HAND_CONNECTIONS
        )

# Compteur 

        doigts_leves = 0

 # Ici pour chaque doigt : si le bout est plus élevé que l'articulation
 
        
        if main.landmark[8].y < main.landmark[5].y:
           doigts_leves += 1
    
        if main.landmark[12].y < main.landmark[9].y:
           doigts_leves += 1
    
        if main.landmark[16].y < main.landmark[13].y:
           doigts_leves += 1
    
        if main.landmark[20].y < main.landmark[17].y:
           doigts_leves+= 1
        
        if main.landmark[4].x > main.landmark[1].x:
           doigts_leves += 1

        
        
        print("Doigt levé", doigts_leves)
          
        if doigts_leves == 0:
           geste_actuel = "poing fermer"
        elif doigts_leves == 1:
           geste_actuel = "chut"
        elif doigts_leves == 5:
           geste_actuel = "Main ouverte"
        else:
            geste_actuel = "Inconu au bataillons les reuf"
    

    # Comparaison avec intégration de geste

        if geste_actuel != geste_precedent:
           print("Nouveau geste :", geste_actuel)
           
           if geste_actuel == "Main ouverte":
             threading.Thread(target= dire_bonjour, args= (2,50)).start()

           elif geste_actuel == "chut":
             threading.Thread(target= non_non, args=(2,50)).start()


           elif geste_actuel == "poing fermer":
              threading.Thread(target= position_repos, args=(1,50)).start()

            
              
           geste_precedent = geste_actuel
           

        
     


    cv2.imshow("Detection de main", image)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()