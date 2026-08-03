"""On est le 30 juillet 2026 :
Comment je pourrais représenter proprement un objet astronomique avec son nom, sa masse et son type ?
Il s'agit de la version 2 de mon simulateur de trou noir en fonction du soleil et à l'aide du rayon de Schwitz....
Dans cette ersion 2 j'aimerais pouvoir simuler un trou noir par rapport à n'importe lequel élément que ce soit le soleil, les planètes, les étoiles.
Je veux pouvoir tout simuler."""

# Pour rendre plus dynamique mon programme je peux intégrer un système de dictionnaire ? 
# J'aimerais séparer mes dictionnaires en plusieurs section : Stellaire, intermediaire, super massif 


black_holes ={

    "stellars":{

        "GaiaBH3" : {

            'Nom' : 'GaiaBH3',
            'Type' : 'Stellar',
            'Constellation' : 'Aquila',
            'masse_solaire' : 33.08,
            'Distance_ly' : 1936,
            'Distance_incertaine' : 9
        },
        
        "Cygnus X-1": {

            'Nom' : 'Cygnus X-1',
            'Type' : 'Stellar',
            'Constellation' : 'Cygne',
            'masse_solaire' : 8.7,
            'Distance_ly' : 7300,
            'Distance_incertaine' : 300
        },

        "IL Lupi": {

            'Nom' : 'IL Lupi',
            'Type' : 'Stellar',
            'Constellation' : 'Lupus',
            'masse_solaire' : 9.4,
            'Distance_ly' : 17000,
            'Distance_incertaine' : "Inconnu",

        }
    },

    "Intermediate": {

        "Messier 15": {
        
            'Nom' : 'Messier 15',
            'Type' : 'Intermediate',
            'Constellation' : 'Pegasus',
            'masse_solaire' : 4000,
            'Distance_ly' : 33600,
            'Distance_incertaine' : "Inconnu",

        },

        "HLX-1": {

            'Nom' : 'HLX-1',
            'Type' : 'Intermediate',
            'Constellation' : 'Phoenix',
            'masse_solaire' : 20000,
            'Distance_ly' : 290e6,
            'Distance_incertaine' : "Inconnu",


        },

        "GCIRS 13E": {

            'Nom' : 'GCIRS 13E',
            'Type' : 'Intermediate',
            'Constellation' : 'Sagittarius',
            'masse_solaire' : 1300,
            'Distance_ly' : 26000,
            'Distance_incertaine' : "Inconnu",


        },

    },

    "Supermassif":{

        "Sagittarius A*": {

            'Nom' : 'Sagittarius A*',
            'Type' : 'Supermassif',
            'Constellation' : 'Sagittarius',
            'masse_solaire' : 4.3e6,
            'Distance_ly' : 27000,
            'Distance_incertaine' : "Inconnu",
        
        },

        "Phoenix A": {

            'Nom' : 'Phoenix A',
            'Type' : 'Supermassif',
            'Constellation' : 'Phénix',
            'masse_solaire' : 100e9,
            'Distance_ly' : 5.7e9,
            'Distance_incertaine' : "Inconnu",

        },

        "NGC 4889":{

            'Nom' : 'NGC 4889',
            'Type' : 'Supermassif',
            'Constellation' : 'Coma Berenices',
            'masse_solaire' : 21e9,
            'Distance_ly' : 308e6,
            'Distance_incertaine' : "Inconnu",

        }
    },

}

"""On est le 31 juillet 2026 et hier soir j'ai terminer de créer un dictionnaire regroupant seulement des black holes.
Elle sont trier par catégories : stellaires, intermediaire, supermassif. Maintenant je vais créer un deuxième dictionnaire,
regroupant en "vrac" des objects astronomique."""  

# Je pensais finalement faire une catégorie planète mais j'hésite, je pense que pour le black hole V3 je développerais un peu plus.
# Pour les planète la distance est en année lumière également

objects_astronomiques={

    "Terre":{
        'Nom' : 'Terre',
        'Type' : 'Object celeste',
        'Constellation' : 'Aucune',
        'masse_solaire' : 3.003e-6,
        'Distance_ly' : 0.0000158,
        'Distance_incertaine' : "Inconnu",
        'Sattelite': "Lune"

    },

    "Mercure":{
         'Nom' : 'Mercure',
         'Type' : 'Object celeste',
         'Constellation' : 'Aucune',
         'masse_solaire' : 1.66e-7,
         'Distance_ly' : 0.0000061,
         'Distance_incertaine' : "Inconnu",
         'Sattelite': "Inconnu"
        
    },

    "Mars":{
        'Nom' : 'Mars',
        'Type' : 'Object celeste',
        'Constellation' : 'Aucune',
        'masse_solaire' : 3.23e-7,
        'Distance_ly' : 0.0000240,
        'Distance_incertaine' : "Inconnu",
        'Sattelite': "Phobos, Déimos"

    },

    "Betelgeuse":{

        'Nom' : 'Betelgeuse',
        'Type' : 'Supergéante rouge',
        'Constellation' : 'Orion',
        'masse_solaire' : 20,
        'Distance_ly' : 700,
        'Distance_incertaine' : "Inconnu",
        'Sattelite': "Aucune",
        'Temperature': 3600,
        'Luminosite': 87100,
        'Magnitude absolue': -5.85,

    },

    "Sirius":{

        'Nom' : 'Sirius',
        'Type' : 'Etoile blanche',
        'Constellation' : 'Grande chien',
        'masse_solaire' : 2.06,
        'Distance_ly' : 8.6,
        'Distance_incertaine' : "Inconnu",
        'Sattelite': "Aucune",
        'Temperature': 9940,
        'Luminosite': 25.4,
        'Magnitude absolue' : 1.42,

    },

    "Alpha cephei":{
        'Nom' : 'Alpha cephei',
        'Type' : 'Sous geante',
        'Constellation' : 'Céphée',
        'masse_solaire' : 2,
        'Distance_ly' : 49.05,
        'Distance_incertaine' : 0.08,
        'Sattelite': "Hipparcos",
        'Temperature': 7700,
        'Luminosite': 19.6,
        'Magnitude absolue': 2.44,


    },

    "Polaris": {

        'Nom' : 'Polaris',
        'Type' : 'Supergeante jaune',
        'Constellation' : 'Petite ourse',
        'masse_solaire' : 8,
        'Distance_ly' : 430,
        'Distance_incertaine' : "Inconnu",
        'Sattelite': "Aucun",
        'Temperature': 7100,
        'Luminosite': 2000,
        'Magnitude absolue': -3.6,
        


    }


}

# J'ai terminer pour le moment les dico je vais commencer a définir des fonctions afin de les introduire plus facilement dans des boucles


# Avant je vais mettre la liste qui comporte les constante, et la masse du soleil ainsi que la vitesse de la lumière
# Petit rappelle de la formule : rayon de Schwarzschild = rayon = 2 * G * masse / c**2

masse_soleil = 1.989e30
G = 0.0000000000667
c = 300000000

# Maintenant je peux attaquer la fonction qui comportera la formule

def schwarzschild_radius(masse_soleil):
    radius = 2 * G * masse_soleil / c**2
    return round(radius,2)


# On parcourt black_holes étage par étage
# categorie = le nom de l'étage ("stellars", "Intermediate", "Supermassif")
# trous_noirs = tous les trous noirs de cet étage (temporaire, change à chaque tour)

for categorie, trous_noirs in black_holes.items():

    # On parcourt chaque trou noir dans l'étage actuel
    # nom = le nom du trou noir ("GaiaBH3", "Cygnus X-1", etc.)
    # infos = toutes les données de ce trou noir (temporaire, change à chaque tour)

    for nom, infos in trous_noirs.items():

        # On prend la masse_solaire dans les infos du trou noir
        # On la multiplie par masse_soleil pour avoir la masse en kg
        # On passe le résultat à la fonction trou_noir() qui calcule le rayon

        #print(nom, ":", schwarzschild_radius(infos['masse_solaire'] * masse_soleil))
        
    # On parcourt simplement un "étage" des objects astronomiques 

   # for nom, infos in objects_astronomiques.items():
       # print(nom, ":", schwarzschild_radius(infos['masse_solaire']* masse_soleil))

    #  Intégration des conditions pour construire un menu intéractif puis la classification automatique des black holes selon leur catégorie.

      while True:

        choix_utilisateur = int(input("1.Simuler un objet astronomique""\n""2.Explorer les trous noirs connus""\n""3.Comparer des trous noirs""\n""4.Créer un objet personnalisé""\n""5.Quitter""\n"))

        if choix_utilisateur ==1:
            print("Simulation en cours...")
            choix_objet = int(input("Quel objet ?\n1.Terre\n2.Mercure\n3.Mars\n4.Betelgeuse\n5.Sirius\n6.Alpha cephei\n7.Polaris\n"))
            if choix_objet == 1:
               print("OBJET :", objects_astronomiques['Terre']['Nom'])
               print("Type :", objects_astronomiques['Terre']['Type'])
               print("Rayon de Schwarzschild :", schwarzschild_radius(objects_astronomiques['Terre']['masse_solaire'] * masse_soleil), "m")
            elif choix_objet ==2:
                print("OBJET :", objects_astronomiques['Mercure']['Nom'])
                print("Type :", objects_astronomiques['Mercure']['Type'])
                print("Rayon de Schwarzschild :", schwarzschild_radius(objects_astronomiques['Mercure']['masse_solaire'] * masse_soleil), "m")
            elif choix_objet == 3:
                print("OBJET :", objects_astronomiques['Mars']['Nom'])
                print("Type :", objects_astronomiques['Mars']['Type'])
                print("Rayon de Schwarzschild :", schwarzschild_radius(objects_astronomiques['Mars']['masse_solaire'] * masse_soleil), "m")
            elif choix_objet == 4:
                print("OBJET :", objects_astronomiques['Betelgeuse']['Nom'])
                print("Type :", objects_astronomiques['Betelgeuse']['Type'])
                print("Rayon de Schwarzschild :", schwarzschild_radius(objects_astronomiques['Betelgeuse']['masse_solaire'] * masse_soleil), "m")
            elif choix_objet ==5:
                print("OBJET :", objects_astronomiques['Sirius']['Nom'])
                print("Type :", objects_astronomiques['Sirius']['Type'])
                print("Rayon de Schwarzschild :", schwarzschild_radius(objects_astronomiques['Sirius']['masse_solaire'] * masse_soleil), "m")
            elif choix_objet ==6:
                print("OBJET :", objects_astronomiques['Alpha cephei']['Nom'])
                print("Type :", objects_astronomiques['Alpha cephei']['Type'])
                print("Rayon de Schwarzschild :", schwarzschild_radius(objects_astronomiques['Alpha cephei']['masse_solaire'] * masse_soleil), "m")
            elif choix_objet ==7:
                print("OBJET :", objects_astronomiques['Polaris']['Nom'])
                print("Type :", objects_astronomiques['Polaris']['Type'])
                print("Rayon de Schwarzschild :", schwarzschild_radius(objects_astronomiques['Polaris']['masse_solaire'] * masse_soleil), "m")



        elif choix_utilisateur ==2:
            print("Exploration en cours...")
            for categorie, trous_noirs in black_holes.items():
                print(categorie, ":")
                for nom, infos in trous_noirs.items():
                    print(nom, ":", schwarzschild_radius(infos['masse_solaire'] * masse_soleil))
                    if infos['masse_solaire'] < 100:
                        print("Catégorie : Stellar")
                    elif infos['masse_solaire'] >= 100 and infos['masse_solaire'] < 100000:
                        print("Catégorie : Intermediate")
                    else:
                        print("Catégorie : Supermassif")
                        

        elif choix_utilisateur == 3:
            print("Comparaison en cours...")
            
            # Étape 1 : construire les listes
            liste_trous_noirs = []
            liste_masses_trous_noirs = []
            for categorie, trous_noirs in black_holes.items():
                for nom, infos in trous_noirs.items():
                    liste_trous_noirs.append(nom)
                    liste_masses_trous_noirs.append(infos['masse_solaire'])

            # Étape 2 : afficher la liste
            for i in range(len(liste_trous_noirs)):
                print(i + 1, ".", liste_trous_noirs[i])

            # Étape 3 : les deux choix
            choix_comparaison1 = int(input("Premier trou noir : ")) - 1
            choix_comparaison2 = int(input("Deuxième trou noir : ")) - 1

            # Étape 4 : calcul
            masse1 = liste_masses_trous_noirs[choix_comparaison1]
            masse2 = liste_masses_trous_noirs[choix_comparaison2]
            radius1 = schwarzschild_radius(masse1 * masse_soleil)
            radius2 = schwarzschild_radius(masse2 * masse_soleil)

            # Étape 5 : affichage
            print("Comparaison entre", liste_trous_noirs[choix_comparaison1], "et", liste_trous_noirs[choix_comparaison2])
            print(liste_trous_noirs[choix_comparaison1], ":", radius1, "m")
            print(liste_trous_noirs[choix_comparaison2], ":", radius2, "m")
            print(liste_trous_noirs[choix_comparaison1], "est", round(radius1 / radius2, 2), "fois plus grand que", liste_trous_noirs[choix_comparaison2])

        

        elif choix_utilisateur ==4:
            print("Création en cours...")
            choix_trou_noir = (input("Choisir un trou noir à créer : "))
            masse_solaire = int(input("Masse en masse solaire : "))  
            rayon_schwarzschild = schwarzschild_radius(masse_solaire * masse_soleil)
            print("Rayon de Schwarzschild :", rayon_schwarzschild, "m")
            if masse_solaire < 100:
                print("Catégorie : Stellar")
            elif masse_solaire >= 100 and masse_solaire < 100000:
                print("Catégorie : Intermediate")
            else:
                print("Catégorie : Supermassif")

        elif choix_utilisateur ==5:
            print("Au revoir")
            break
            
        
                                      
        
            



        
