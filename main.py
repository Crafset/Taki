#! /usr/bin/python

import pywifi
from pywifi import const

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()  # Initialise l'interface Wi-Fi
    iface = wifi.interfaces()[0]  # Sélectionne la première interface Wi-Fi

    iface.disconnect()  # Déconnexion de tout réseau précédemment connecté

    profile = pywifi.Profile()  # Crée un nouveau profil Wi-Fi
    profile.ssid = ssid  # Nom du réseau Wi-Fi
    profile.auth = const.AUTH_ALG_OPEN  # Type d'authentification (ici, sans mot de passe)
    profile.akm.append(const.AKM_TYPE_NONE)  # Algorithme de gestion des clés (ici, sans mot de passe)

    iface.remove_all_network_profiles()  # Supprime tous les profils Wi-Fi existants
    tmp_profile = iface.add_network_profile(profile)  # Ajoute le nouveau profil Wi-Fi

    iface.connect(tmp_profile)  # Connecte à un réseau Wi-Fi spécifique

    # Attend que la connexion soit établie
    while iface.status() == const.IFACE_CONNECTING:
        pass

    if iface.status() == const.IFACE_CONNECTED:  # Vérifie si la connexion est réussie
        print('Connecté à', ssid)
    else:
        print('Échec de la connexion à', ssid)

# Exemple d'utilisation
ssid = 'NomDuReseauWiFi'
password = 'MotDePasseWiFi'

connect_to_wifi(ssid, password)
