from pymycobot import MyCobot280
import time

mc= MyCobot280('COM3', 115200)
time.sleep(2)

#======= Mes Fonctions ======

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
        mc.send_angles([0, -95, -20,20, 40,0], vitesse)
        time.sleep(60/vitesse)
        mc.send_angles([0, -95, -20,20, -40, 0], vitesse)
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

#======= Programme Principal =====

dire_bonjour(3, 45)
non_non(6,90)
oui_oui(2,30)
position_repos()