import os

name = input("Enter name : ")
hostname = input("Enter hostname")

print("ip_boot")
print("ip_logger")
print("ip_scanner")

choix = input("Enter your choix : ")

os.system(f"python3 /home/{name}/tools/{choix}.py ")







