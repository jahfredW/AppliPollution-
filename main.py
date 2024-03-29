import meteo
import pollution
import datetime
import affichage_meteo
from meteo_common import *
from meteo_utils import *
import requests
from tkinter import *
import graphique

if __name__ == '__main__':


    meteoLoop = True

    while meteoLoop:

        period = 0
        loop = False

        # on définit un variable pour contenir le nom de la ville pour laquelle afficher la météo
        ville_en_cours = ""

        # on affiche l'écran d'accueil qui permet à l'utilisateur de rechercher une ville
        affichage_meteo.afficher_ecran_accueil()

        # on récupère le choix fait par l'utilisateur
        choix_utilisateur = int(input("Quel est votre choix (1 ou 2) ?> "))

        # si l'utilisateur choisit la première proposition de l'écran d'accueil, alors on lui demande
        # de saisir le nom de la ville qu'il recherche (une partie du nom suffit pour lancer la recherche)
        if choix_utilisateur == 1:

            # on récupère le texte de l'utilisateur saisie à l'écran et on le stock dans la variable choix_ville
            choix_ville = input("Quelle ville recherchez-vous ?> ")
            # on récupère le résultat de la recherche des villes et on le stock dans la variable liste_ville
            liste_villes = meteo.recherche_ville(choix_ville)
            # on vérifie si la recherche à bien renvoyé un résultat (pour ne pas travailler sur des données inexistantes et générer une erreur technique)
            if liste_villes == None:
                print("Désolé, aucune ville corespondante n'a été trouvée.")
            else:
                # si la variable existe mais que le nombre de ville est égale à zéro, on prévient l'utilisateur
                if len(liste_villes) == 0:
                    print("Désolé, aucune ville corespondante n'a été trouvée.")
                else:
                    # construction d'un dictionnaire pour classer les villes et permettre à l'utilisateur
                    # de les sélectionner par un numéro
                    choix_ville_recherche = {}
                    numero_choix = 1
                    for ville in liste_villes:
                        choix_ville_recherche[numero_choix] = ville
                        numero_choix += 1

                    # on affiche maintenant le résultat de la recherche à l'utilisateur pour qu'il puisse choisir une ville à consulter
                    affichage_meteo.afficher_liste_ville(choix_ville_recherche)

                    # en fonction du choix de l'utilisateur, on récupère la ville choisie.
                    # ici, petite astuce : comme on utilise un dictionnaire avec le nom de de la ville et un index, le choix de l'utilisateur est en fait
                    # l'index du dictionnaire, ce qui permet de récupérer directement le nom de la ville grâce à l'index...
                    ville_en_cours = choix_ville_recherche[
                        int(input("Pour consulter la météo d'une ville, tapez son numéro dans la liste> "))]

                    # on affiche maintenant les résultats, c'est à dire les infromations météos relatives à la ville choisie par l'utilisateur.
                    # pour cela on utilise une fonction d'affichage en premier pour l'entête, qui permet d'obtenir les valeurs nécéssaires en fonction de la ville choisie
                    affichage_meteo.afficher_en_tete(ville_en_cours,
                                                     meteo.get_avis_meteo_detaille_prevision(ville_en_cours, period),
                                                     meteo.get_temperature_actuelle(ville_en_cours)
                                                     ,
                                                     meteo.get_pression_athmospherique_prevision(ville_en_cours, period=0),
                                                     meteo.get_humidite_prevision(ville_en_cours, period=0)
                                                     , meteo.get_vent_vitesse_prevision(ville_en_cours, period=0),
                                                     meteo.get_vent_orientation_prevision(ville_en_cours, period=0))

                    # l'entête est maintenant affichée pour l'utilisateur, avec les informations météos actuelles sur la ville, mais on souhaite également afficher
                    # les prévisions à 7 jours.
                    # pour cela on construit une liste qui va stockée les valeurs de prévisions pour les 7 prochains jours
                    liste_previsions = []

                    liste_previsions.append(
                        construire_affichage_prevision_temperature(ville_en_cours, "T° jour", PREVISION_TEMPERATURE_JOUR))
                    liste_previsions.append(
                        construire_affichage_prevision_temperature(ville_en_cours, "T° min", PREVISION_TEMPERATURE_MINI))
                    liste_previsions.append(
                        construire_affichage_prevision_temperature(ville_en_cours, "T° max", PREVISION_TEMPERATURE_MAXI))
                    liste_previsions.append(
                        construire_affichage_prevision_temperature(ville_en_cours, "T° mat", PREVISION_TEMPERATURE_MATIN))
                    liste_previsions.append(construire_affichage_prevision_temperature(ville_en_cours, "T° midi",
                                                                                       PREVISION_TEMPERATURE_APRES_MIDI))
                    liste_previsions.append(
                        construire_affichage_prevision_temperature(ville_en_cours, "T° nuit", PREVISION_TEMPERATURE_NUIT))
                    liste_previsions.append(construire_affichage_prevision_pression_athmospherique(ville_en_cours))
                    liste_previsions.append(construire_affichage_prevision_humidite(ville_en_cours))
                    liste_previsions.append(construire_affichage_prevision_vent_vitesse(ville_en_cours))
                    liste_previsions.append(construire_affichage_prevision_vent_orientation(ville_en_cours))
                    liste_previsions.append(construire_affichage_prevision_avis_meteo_detaille(ville_en_cours))

                    # une fois qu'on a les informations en mémoire (dans la liste) pour les prévisions météo sur les 7 prochains jours,
                    # on peut les afficher à l'écran avec un formatage sur les 7 prochains jours
                    affichage_meteo.afficher_previsions(liste_previsions)
                    # On récupère à présent l'avis météo, c'est une chaîne de caractère.
                    # En fonction de sa valeur, on va afficher une image différentes à l'utilisateur
                    # image = représentation sous forme de caractères présent dans une fichier
                    avis_meteo_actuel = meteo.get_avis_meteo_detaille(ville_en_cours)

                    if avis_meteo_actuel == STATUT_API_NUAGEUX:
                        affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_NUAGEUX)
                    elif avis_meteo_actuel == STATUT_API_PEU_NUAGEUX:
                        affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_ECLAIRCIES)
                    elif avis_meteo_actuel == STATUT_API_PARTIELLEMENT_NUAGEUX:
                        affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_ECLAIRCIES)
                    elif avis_meteo_actuel == STATUT_API_CIEL_DEGAGE:
                        affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_SOLEIL)
                    elif avis_meteo_actuel == STATUT_API_LEGERE_PLUIE:
                        affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_PLUIE)
                    elif avis_meteo_actuel == STATUT_API_LEGERE_COUVERT:
                        affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_NUAGEUX)
                    else:
                        print("l'image pour la prévision actuelle n'est pas configurée, pensez à mettre à jour le code")

                    meteoLoop = affichage_meteo.continuer()

        elif choix_utilisateur == 2:
            # implémentation du choix graphique ou bilan
            a = affichage_meteo.afficher_ecran_pollution()

            # on récupère le texte de l'utilisateur saisie à l'écran et on le stock dans la variable choix_ville

            choix_ville = input("Quelle ville recherchez-vous ?> ")

            # on récupère le résultat de la recherche des villes et on le stock dans la variable liste_ville

            liste_villes = meteo.recherche_ville(choix_ville)

            # on vérifie si la recherche à bien renvoyé un résultat (pour ne pas travailler sur des données inexistantes et générer une erreur technique)

            if liste_villes == None:

                print("Désolé, aucune ville corespondante n'a été trouvée.")

            else:

                # si la variable existe mais que le nombre de ville est égale à zéro, on prévient l'utilisateur

                if len(liste_villes) == 0:

                    print("Désolé, aucune ville corespondante n'a été trouvée.")

                else:

                    # construction d'un dictionnaire pour classer les villes et permettre à l'utilisateur

                    # de les sélectionner par un numéro

                    choix_ville_recherche = {}

                    numero_choix = 1

                    for ville in liste_villes:
                        choix_ville_recherche[numero_choix] = ville

                        numero_choix += 1

                    # on affiche maintenant le résultat de la recherche à l'utilisateur pour qu'il puisse choisir une ville à consulter

                    affichage_meteo.afficher_liste_ville(choix_ville_recherche)

                    # en fonction du choix de l'utilisateur, on récupère la ville choisie.

                    # ici, petite astuce : comme on utilise un dictionnaire avec le nom de de la ville et un index, le choix de l'utilisateur est en fait

                    # l'index du dictionnaire, ce qui permet de récupérer directement le nom de la ville grâce à l'index...

                    ville_en_cours = choix_ville_recherche[
                        int(input("Pour consulter les infos de la ville, tapez son numéro dans la liste> "))]

                    # on affiche maintenant les résultats, c'est à dire les infromations météos relatives à la ville choisie par l'utilisateur.

                    # pour cela on utilise une fonction d'affichage en premier pour l'entête, qui permet d'obtenir les valeurs nécéssaires en fonction de la ville choisie

                if a == 1:

                    affichage_meteo.afficher_en_tetePol(ville_en_cours, pollution.get_date(ville_en_cours, period=0),
                                                        pollution.get_aqi(ville_en_cours, period=0),

                                                        pollution.get_nh3(ville_en_cours, period=0),
                                                        pollution.get_co(ville_en_cours, period=0),
                                                        pollution.get_pm10_j5(ville_en_cours, period=0),

                                                        pollution.get_pm25_j5(ville_en_cours, period=0),
                                                        pollution.get_so2(ville_en_cours, period=0))

                    # l'entête est maintenant affichée pour l'utilisateur, avec les informations météos actuelles sur la ville, mais on souhaite également afficher

                    # les prévisions à 7 jours.

                    # pour cela on construit une liste qui va stockée les valeurs de prévisions pour les 7 prochains jours

                    liste_pollution = []

                    liste_pollution.append(construire_affichage_aqi(ville_en_cours))
                    liste_pollution.append(construire_affichage_co(ville_en_cours))
                    liste_pollution.append(construire_affichage_pm10(ville_en_cours))
                    liste_pollution.append(construire_affichage_pm25(ville_en_cours))
                    liste_pollution.append(construire_affichage_nh3(ville_en_cours))
                    liste_pollution.append(construire_affichage_so2(ville_en_cours))

                    # une fois qu'on a les informations en mémoire (dans la liste) pour les prévisions météo sur les 7 prochains jours,

                    # on peut les afficher à l'écran avec un formatage sur les 7 prochains jours

                    affichage_meteo.afficher_previsions(liste_pollution)

                    # affichage_meteo.afficher_previsions(liste_previsions)

                    # On récupère à présent l'avis météo, c'est une chaîne de caractère.

                    # En fonction de sa valeur, on va afficher une image différentes à l'utilisateur

                    # image = représentation sous forme de caractères présent dans une fichier

                    # avis_meteo_actuel = meteo.get_avis_meteo_detaille(ville_en_cours)

                    indice_en_cours = pollution.get_aqi(ville_en_cours, 0)

                    if indice_en_cours == 1:

                        affichage_meteo.afficher_image_meteo(6)

                    # if avis_meteo_actuel == STATUT_API_NUAGEUX:

                    #     affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_NUAGEUX)

                    # elif avis_meteo_actuel == STATUT_API_PEU_NUAGEUX:

                    #     affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_ECLAIRCIES)

                    # elif avis_meteo_actuel == STATUT_API_PARTIELLEMENT_NUAGEUX:

                    #     affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_ECLAIRCIES)

                    # elif avis_meteo_actuel == STATUT_API_CIEL_DEGAGE:

                    #     affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_SOLEIL)

                    # elif avis_meteo_actuel == STATUT_API_LEGERE_PLUIE:

                    #     affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_PLUIE)

                    # elif avis_meteo_actuel == STATUT_API_LEGERE_COUVERT:

                    #     affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_NUAGEUX)

                    else:

                        print("l'image pour la prévision actuelle n'est pas configurée, pensez à mettre à jour le code")

                if a == 2:

                    while not loop:
                        b = affichage_meteo.afficher_liste_polluants()
                        graphique.draw_graph(ville_en_cours, b)
                        c = int(input("Consulter un autre graphique ? (1->Oui, 2->Quitter "))

                        if c == 2:
                            loop = True
                            print(" Au revoir !")

                        else:
                            pass


        elif choix_utilisateur == 3:

            # on récupère le texte de l'utilisateur saisie à l'écran et on le stock dans la variable choix_ville

            choix_ville = input("Quelle ville recherchez-vous ?> ")

            # on récupère le résultat de la recherche des villes et on le stock dans la variable liste_ville

            liste_villes = meteo.recherche_ville(choix_ville)

            # on vérifie si la recherche à bien renvoyé un résultat (pour ne pas travailler sur des données inexistantes et générer une erreur technique)

            if liste_villes == None:

                print("Désolé, aucune ville corespondante n'a été trouvée.")

            else:

                # si la variable existe mais que le nombre de ville est égale à zéro, on prévient l'utilisateur

                if len(liste_villes) == 0:

                    print("Désolé, aucune ville corespondante n'a été trouvée.")

                else:

                    # construction d'un dictionnaire pour classer les villes et permettre à l'utilisateur

                    # de les sélectionner par un numéro

                    choix_ville_recherche = {}

                    numero_choix = 1

                    for ville in liste_villes:
                        choix_ville_recherche[numero_choix] = ville

                        numero_choix += 1

                    # on affiche maintenant le résultat de la recherche à l'utilisateur pour qu'il puisse choisir une ville à consulter

                    affichage_meteo.afficher_liste_ville(choix_ville_recherche)

                    # en fonction du choix de l'utilisateur, on récupère la ville choisie.

                    # ici, petite astuce : comme on utilise un dictionnaire avec le nom de de la ville et un index, le choix de l'utilisateur est en fait

                    # l'index du dictionnaire, ce qui permet de récupérer directement le nom de la ville grâce à l'index...

                    ville_en_cours = choix_ville_recherche[
                        int(input("Pour consulter les infos de la ville, tapez son numéro dans la liste> "))]

                root = Tk()
                root.geometry("300x300")
                root.title(f"{ville_en_cours}")


                def display_city_name(ville_en_cours):
                    ville_label = Label(root, text=f"{ville_en_cours}")
                    ville_label.config(font=("Consolas", 35))
                    ville_label.pack(side='top')


                def display_stats(pollution):
                    aqi = Label(root, text=f"Indice: {pollution.get_aqi(ville_en_cours, 0)} ")
                    pm10 = Label(root, text=f"Pm10: {pollution.get_pm10_j5(ville_en_cours, 0)} µm/m3")
                    pm25 = Label(root, text=f"Pm2_5: {pollution.get_pm25_j5(ville_en_cours, 0)} µm/m3")

                    aqi.config(font=("Consolas", 28))
                    pm10.config(font=("Consolas", 22))
                    pm25.config(font=("Consolas", 22))

                    aqi.pack(side='top')
                    pm10.pack(side='top')
                    pm25.pack(side='top')


                def display_commentaire():
                    com = Label(root, text=" Vas courir ! ")
                    com.config(font=("Arial", 30))
                    com.pack(side='bottom')


                display_city_name(ville_en_cours)
                display_stats(pollution)
                display_commentaire()

                mainloop()

                meteoLoop = affichage_meteo.continuer()

        else:
            print("Désolé votre choix n'est pas un 1 ou 2, que souhaitez-vous faire ?")
