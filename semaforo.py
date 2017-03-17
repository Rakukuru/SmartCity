#!/usr/bin/python

# Semaforo
from socket import *
import time
import threading

# Default server
#serverName = '192.168.60.238'
serverName = '127.0.0.1'
serverPort = 5005
messize = len("sos")

def green():
    print("Green")
    time.sleep(10)

def red():
    print("Red")
    time.sleep(10)

def luces():
    while 1:
        try:
            green()
        except clientSocket.recv(messize) == "sos":
            green()
        try:
            red()
        except clientSocket.recv(messize) == "sos":
            green()

# Optional server port number
#if (len(sys.argv) > 2):
#	serverPort = int(sys.argv[2])

# Request IPv4 and TCP communication
clientSocket = socket(AF_INET, SOCK_STREAM)

#clientSocket.setblocking(0)

# The welcoming port that clients first use to connect
clientSocket.bind((serverName, serverPort))

# Start listening on the welcoming port
clientSocket.listen(1)
print('The server is ready to receive')


print("waiting for connection")
connection, client_address = clientSocket.accept()

# Traffic light function
luces()

