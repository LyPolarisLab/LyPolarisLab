"""
MyCobot 280 - Connection Test

First experiment:
- Connect Python with the robot
- Check robot communication
- Read robot information

"""



from pymycobot import MyCobot280
import time 

#Connexion au robot sur le port COM3
mc = MyCobot280('COM3', 115200)
time.sleep(2) # Attente de 2 secondes pour que le robot se connecte correctement

#Test : demander la version du firmware 
print("Version : ", mc.get_system_version())

#Test : Lire les angles actuels des 6 joints du robot
print("Angles actuels : ", mc.get_angles())

#Configuration des angles de calibration pour chaque joint du robot
mc.send_angles([0, 0, 0, 0, 0, 0], 30)

