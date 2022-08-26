import os
import subprocess
from datetime import datetime
import pyttsx3
import requests
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#heure
monHeure = datetime.now()
monHeure1 = monHeure.strftime("%H heure-%M minutes et-%S secondes")

#jour
monJour = datetime.now()
monJour1 = monJour.strftime("%d-%m-%Y")

print(f"{monJour1} {monHeure1}")

#PARAMETRE
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'french')

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    try:
        response = recognizer.recognize_google(audio,language='fr-FR')
    except:
        response = "[-]rien a enttendre"
    return response

speak("Bonjour comment sa va ?")
while True:
    #speak("Puis-je vous aider ?")
    voice = recognize_speech().lower()
    print(f"[+]{voice}")
    #CHROME
    if 'tu as qui ouvre chrome' in voice:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.maximize_window()
        speak('ouverture de chrome')
    #GOOGLE
    if 'tu as qui lance google' in voice:
        speak('ouverture de google')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://google.com')
    elif 'fais une recherche' in voice:
        while True:
            speak('Je vous écoute')
            query = recognize_speech()
            if query != 'Erreur':
                break
        element = driver.find_element_by_name('q')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    #Changer de site
    elif 'tu as qui change de site' in voice:
        num_tabs = len(driver.window_handles)
        cur_tab = 0
        for i in range(num_tabs):
            if driver.window_handles[i] == driver.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i + 1
                    break
        driver.switch_to_window(driver.window_handles[cur_tab])
    #ferme l'onglet
    elif 'tu as qui ferme longlet' in voice:
        speak('Daccord')
        driver.close()
    #page precedente
    elif 'tu as qui va à la page précédente' in voice:
        driver.back()
    #page suivante
    elif 'tu as qui va à la page suivante' in voice:
        driver.forward()
    #ça va ? rep
    elif 'ça va et toi' in voice:
        speak('daccord moi aussi, Puis-je vous aider ?')
    #ça va ? question
    elif 'ça va tu as qui' in voice:
        speak('très bien merci et toi ?')
    #non
    elif 'non' in voice:
        speak('daccord pas de souci')
    #oui
    elif 'oui' in voice:
        speak('daccord que puis-je faire pour vous')
    #merci
    elif 'merci' in voice:
        speak('derien tout le plaisir est pour moi !')

    #tu es la ?
    elif 'tu es là tu as qui' in voice:
        speak('oui je suis toujours la, pourquoi ?')

    #heure
    elif 'tu as qui quelle heure est-il' in voice:
        speak(f"il est {monHeure1}")
    #jour
    elif 'tu as qui quel jour sommes-nous' in voice:
        speak(f"On est le {monJour1}")

    #help
    elif 'tu as qui quelles sont les commandes' in voice:
        speak("Vous pouvez me demander de lancer une application, me demander le jour et l'heure, envoyer des messages, puis ouvrir chrome, et le controler avec google. Un ficher sera fait sous le nom de cmd dans mon dossier avec toutes les commandes.")
        fic = open("cmd.txt", "w", encoding='UTF-8')

        fic.write("ouvrir chrome : taki ouvre chrome\n")
        fic.write("lancer google : taki lance google\n")
        fic.write("faire une recherche sur google : fais une recherche\n")
        fic.write("ferme l'onglet chrome: taki ferme l'onglet\n")
        fic.write("aller a la page precedente : taki va à la page precedente\n")
        fic.write("aller a la page suivante : taki va à la page suivante\n")
        fic.write("dire ça va en reponse  : ça va et toi\n")
        fic.write("dire ça va en question  : ça va taki\n")
        fic.write("non : non\n")
        fic.write("oui : oui\n")
        fic.write("merci : merci\n")
        fic.write("demander si elle est la : tu es là taki\n")
        fic.write("demander l'heure : taki quelle heure est-il\n")
        fic.write("demander le jour : taki quel jour sommes-nous\n")
        fic.write("help : taki quelles sont les commandes\n")
        fic.write("recherche google direct : taki fait une recherche google\n")
        fic.write("ouvrir spotify : taki ouvre spotify\n")
        fic.write("ouvrir la calculatrice : taki ouvre la calculatrice\n")
        fic.write("ouvrir Opera : taki ouvre opera\n")
        fic.write("ouvrir le cmd : taki ouvre le cmd\n")
        fic.write("quitter chrome : taki ferme chrome\n")
        fic.write("fermer le script : taki ferme-toi\n")
        fic.write("envoyer un sms : taki envoie un message (une fois par jour seulement!)\n")

        fic.close()

    elif 'tu as qui envoie un message' in voice:
        while True:
            speak('a quelle numero voulez vous envoyer un message ?')
            query = recognize_speech()
            speak('a quelle message voulez vous envoyer ?')
            query1 = recognize_speech()
            resp = requests.post('https://textbelt.com/text', {
                'phone': f'+33{query}',
                'message': f'{query1}',
                'key': 'textbelt',
            })
            print(resp.json())
            if query != 'Erreur':
                break

    elif 'tu as qui fait une recherche google' in voice:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.maximize_window()
        #speak('ouverture de google')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://google.com')
        while True:
            speak('que voulez vous rechercher ?')
            query = recognize_speech()
            if query != 'Erreur':
                break
        element = driver.find_element_by_name('q')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)


    #run programme

    #spotify
    elif 'tu as qui ouvre spotify' in voice:
        subprocess.call('spotify.exe')

    #calculatrice
    elif 'tu as qui ouvre la calculatrice' in voice:
        subprocess.call('calc.exe')

    #Opera
    elif 'tu as qui ouvre opera' in voice:
        os.system('start opera.exe')

    #cmd
    elif 'tu as qui ouvre le cmd' in voice:
        os.system('start cmd.exe')

    #QUITER CHROME
    elif 'tu as qui ferme chrome' in voice:
        speak('daccord')
        driver.quit()
    #QUITER
    elif 'tu as qui ferme-toi' in voice:
        speak('Daccord bonne journée.')
        driver.quit()
        break

    #else:
        #speak('désolé je ne comprends pas.')