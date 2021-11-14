import pyowm
from datetime import datetime
import requests
from pyowm.utils.config import get_default_config
from pyowm.utils import measurables
from pyowm.utils import timestamps, formatting
import requests

# initialisation des variables du module (le "_" devant le nom des variables est une convention
# pour indiquer qu'elle doivent être utilisées à titre privé dans le module
APIKEY = 'de344c900509e22467e79e19be02d6bb'
_meteo_api_initialized = False
_meteo_api = None  # On force la valeur à "None" pour permettre les tests par la suite (Null dans les autres langages le plus souvent)
_meteo_villes = {}  # Permet de garder en mémoire les informations météo d'une ville, pour ne pas redemander les données à chaque appel (car il existe une limitation d'appel côté API à préserver)


def _get_meteo_api():
    """
    Intialise l'objet _meteo_api qui permet de dialoguer avec l'API de OpenWeatherMap
    :return:
    """

    # les variables sont déclarées global car les valeurs être stockées sont au niveau des variables du module
    # ainsi les autres fonctions du module pour utiliser les variables du module initialisées ici
    # NB : nécessaire car sinon la durée de vie des variables est celle de la durée de vie de la fonction
    global _meteo_api_initialized
    global _meteo_api

    # on vérifie par le boulon que l'initialisation n'a pas été déjà faite, pour ne pas faire
    # des traitements inutiles (consommation de ressources alors qu'on les a déjà)
    if not _meteo_api_initialized:
        config_dict = get_default_config()
        config_dict['language'] = 'fr'
        _meteo_api = pyowm.OWM(APIKEY, config_dict)
        _meteo_api_initialized = True

    # on obtient l'objet API si il avzait déjà été initialisé ou bien si il vient juste de l'être
    # NB : c'est une bonne pratique, ainsi les autres fonction appeleront celle ci pour obtenir l'objet plutôt
    # que d'y accéder directement dans le module.
    # cela évite les accès multiple à la même variable sans contrôle, ainsi on donne un seul point d'accès à la
    # variable d'API météo, en s'assurant que tout les traitement nécessaires ont été effectué (et si il y a un bug,
    # il sera corrigé à un seul endroit (ici dans cette fonction)
    return _meteo_api


def recherche_ville(ville):
    """
    recherche les villes correspondant à la chaîne de caractère donnée en paramètre
    :param ville: chaîne de carcatère qui est le nom de la ville (ou une partie du nom)
    :return: liste des villes trouvées, liste vide si aucun résultat de recherche
    """
    meteo = _get_meteo_api()
    if meteo is not None:
        reg = meteo.city_id_registry()
        villes = reg.ids_for(ville, country='FR',
                             matching='like')  # matching='like' permet de faire une recherche même si on ne connaît pas le nom complet de la ville
        new_list = []
        for ville in villes:
            if ville[1] not in new_list:
                new_list.append(ville[
                                    1])  # ville[1] contient le nom de la ville trouvée, se référent à la documentation de l'API pour les détails des valeurs retournées
        return new_list
    else:
        print("Erreur : l'API météo n'est pas initialisée")


def _get_location(ville, pays):
    meteo = _get_meteo_api()
    reg = meteo.city_id_registry()
    emplacements = reg.locations_for(ville, pays)
    liste = str(emplacements)
    listeSplit = liste.split(',')
    chaine = listeSplit[1]
    chaine = chaine.split('=')
    print(f" La ville de {chaine[1]} a les coordonnées{listeSplit[2]} et{listeSplit[3]}")

    return chaine[1], listeSplit[2], listeSplit[3]


def _get_meteo_ville(ville):
    '''
    Obtient les informations météo courantes d'une ville
    :param ville: nom de la ville
    :return: les informations météo courantes d'une ville
    '''
    global _meteo_villes
    meteo = _get_meteo_api()

    # si la météo d'une ville a déjà été consultée, renvoyer le resultat déjà mémorisé
    if ville in _meteo_villes:
        return _meteo_villes[ville]

    # par sécurité, avant d'utiliser une variable contenant un objet (ici celui d'API), on vérifie qu'il
    # a bien été initialisé au préalable, pour éviter des erreurs techniques
    if meteo is not None:
        # on recherche l'emplacement de la ville (contient lattitude et longitude)
        reg = meteo.city_id_registry()
        emplacements = reg.geopoints_for(ville)
        emplacement = emplacements[0]

        # on obtient les informations météos de la ville
        mgr = meteo.weather_manager()
        meteo_ville = mgr.one_call(lat=emplacement.lat, lon=emplacement.lon, units='metrics')

        # on enregistre en mémoire pour la prochaine demande
        _meteo_villes[ville] = meteo_ville

        # on renvoi la météo demandée pour la ville
        return meteo_ville
    else:
        print("Erreur : l'API météo n'est pas initialisée")


def reception_time(rec_time, timeformat='unix'):
    """Returns the GMT time telling when the forecast was received
            from the OWM Weather API

    :param timeformat: the format for the time value. May be:
        '*unix*' (default) for UNIX time
        '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
        '*date* for ``datetime.datetime`` object instance
    :type timeformat: str
    :returns: an int or a str
    :raises: ValueError

    """
    return formatting.timeformat(rec_time, timeformat)


def _get_pollution_ville(ville):
    '''
    Obtient les informations météo courantes d'une ville
    :param ville: nom de la ville
    :return: les informations météo courantes d'une ville
    '''
    global _meteo_villes
    meteo = _get_meteo_api()

    # si la météo d'une ville a déjà été consultée, renvoyer le resultat déjà mémorisé
    if ville in _meteo_villes:
        return _meteo_villes[ville]

    # par sécurité, avant d'utiliser une variable contenant un objet (ici celui d'API), on vérifie qu'il
    # a bien été initialisé au préalable, pour éviter des erreurs techniques
    if meteo is not None:
        # on recherche l'emplacement de la ville (contient lattitude et longitude)
        pol = meteo.city_id_registry()
        emplacements = pol.geopoints_for(ville)
        emplacement = emplacements[0]

        # on obtient les informations météos de la ville
        pol = meteo.airpollution_manager()
        pol_ville = pol.air_quality_forecast_at_coords(emplacement.lon, emplacement.lat)
        # meteo_ville.air_quality_data
        # on enregistre en mémoire pour la prochaine demande
        # _meteo_villes[ville] = meteo_ville

        # on renvoi la météo demandée pour la ville
        # print(str(reception_time(meteo_ville[0].rec_time)))

        # print(datetime.utcfromtimestamp(meteo_ville[0].ref_time).strftime('%Y-%m-%d %H:%M:%S'))

        return pol_ville

    else:
        print("Erreur : l'API météo n'est pas initialisée")

        date = []
        indice = []
        # for forecast in meteo_ville:
        #     date.append((datetime.utcfromtimestamp(forecast.ref_time).strftime('%Y-%m-%d %H:%M:%S')))

        # print(meteo_ville[0].air_quality_data['co'])
        # print(emplacement.lat)
        # date = []
        # for forecast in meteo_ville:
        #    print(forecast.reference_time(timeformat='date'))


def get_date(ville, period):
    date_ville = _get_pollution_ville(ville)
    date = date_ville[period].reception_time(timeformat='iso')
    return date


"""
                return meteo_ville
            # else:
            #     print("Erreur : l'API météo n'est pas initialisée")


"""


def get_nh3(ville, period):
    meteo = _get_meteo_api()
    if meteo is not None:
        nh3_ville = _get_pollution_ville(ville)
        nh3 = nh3_ville[period].air_quality_data['nh3']
        return nh3
    else:
        print("Erreur : l'API météo n'est pas initialisée")


def get_pm10_j5(ville, period):
    meteo = _get_meteo_api()
    if meteo is not None:
        pm10_ville = _get_pollution_ville(ville)
        pm10 = pm10_ville[period].air_quality_data['pm10']
        return pm10
    else:
        print("Erreur : l'API météo n'est pas initialisée")


def get_co(ville, period):
    meteo = _get_meteo_api()
    if meteo is not None:
        co_ville = _get_pollution_ville(ville)
        co = co_ville[period].air_quality_data['co']
        return co
    else:
        print("Erreur : l'API météo n'est pas initialisée")



def get_pm25_j5(ville, period):
    meteo = _get_meteo_api()
    if meteo is not None:
        pm25_ville = _get_pollution_ville(ville)
        pm25 = pm25_ville[period].air_quality_data['pm2_5']
        return pm25
    else:
        print("Erreur : l'API météo n'est pas initialisée")


def get_aqi(ville, period):
    meteo = _get_meteo_api()
    if meteo is not None:
        aqi_ville = _get_pollution_ville(ville)
        aqi = aqi_ville[period].air_quality_data['aqi']
        return aqi
    else:
        print("Erreur : l'API météo n'est pas initialisée")


def get_temperature_actuelle(ville):
    """
    Obtient la températue actuelle d'une ville en degrés celsius
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :return: la témpérature, en degré celsius
    """
    meteo = _get_meteo_api()
    if meteo is not None:
        meteo_ville = _get_meteo_ville(ville)
        return meteo_ville.current.temperature('celsius').get('temp', None)
    else:
        print("Erreur : l'API météo n'est pas initialisée")


def get_temperature_prevision(ville, type_temperature, period):
    """
    Obtient la température prévue pour une ville
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :param type_temperature: TEMPERATURE, TEMPERATURE_RESSENTIE, PREVISION_TEMPERATURE_MINI, etc... voir valeurs dans meteo_common.py
    :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
    :return: la température en degrés celsius
    """

    meteo_ville = _get_meteo_ville(ville)

    temperature = meteo_ville.forecast_daily[period].temperature('celsius').get(type_temperature, None)
    return temperature


def get_avis_meteo(ville):
    """
    obtient une descrption courte de l'avis météo sous forme de chapine de caractère
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :return: chaîne de caractère qui est la description courte de l'avis météo
    """

    meteo_ville = _get_meteo_ville(ville)
    return meteo_ville.current.status


def get_avis_meteo_detaille(ville):
    """
    obtient l'avis météo détaillé pour la ville recherchée
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :return: avis détaillé
    """

    meteo_ville = _get_meteo_ville(ville)
    return meteo_ville.current.detailed_status


def get_avis_meteo_detaille_prevision(ville, period):
    """
    Obtient la prévision météo détaillée pour une ville et un jour donnés (J, J+1, J+2, etc...)
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
    :return:
    """

    meteo_ville = _get_meteo_ville(ville)
    return meteo_ville.forecast_daily[period].detailed_status


# def get_prevision_pollution(ville):
#     meteo_ville = get_pol(ville)
#     return meteo_ville


def get_humidite_prevision(ville, period):
    """
    Obtient la prévision d'humidité pour une ville et un jour donnés (J, J+1, J+2, etc...)
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
    :return:
    """

    meteo_ville = _get_meteo_ville(ville)
    return meteo_ville.forecast_daily[period].humidity


def get_pression_athmospherique_prevision(ville, period):
    """
    Obtient la prévision de pression athmosphérique pour une ville et un jour donnés (J, J+1, J+2, etc...)
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
    :return:
    """

    meteo_ville = _get_meteo_ville(ville)
    return meteo_ville.forecast_daily[period].pressure.get('press')


def get_vent_vitesse_prevision(ville, period):
    """
    Obtient la prévision de vitesse du vent pour une ville et un jour donnés (J, J+1, J+2, etc...)
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
    :return:
    """

    meteo_ville = _get_meteo_ville(ville)
    kmhour_wind_dict = measurables.metric_wind_dict_to_km_h(
        meteo_ville.forecast_daily[period].wnd)  # permet d'avoir la vitesse en km/h
    return kmhour_wind_dict.get('speed', None)


def get_vent_orientation_prevision(ville, period):
    """
    Obtient la prévision d'orientation du vent pour une ville et un jour donnés (J, J+1, J+2, etc...)
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
    :return:
    """

    meteo_ville = _get_meteo_ville(ville)
    return meteo_ville.forecast_daily[period].wnd.get('deg', None)


def get_probabilite_precipitation_prevision(ville, period):
    """
    Obtient la prévision de la probabilité de précipitation du vent pour une ville et un jour donnés (J, J+1, J+2, etc...)
    :param ville: chaine de caractère représentant la ville sur laquelle porte la recherche
    :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
    :return:
    """

    meteo_ville = _get_meteo_ville(ville)
    return meteo_ville.forecast_daily[period].precipitation_probability
