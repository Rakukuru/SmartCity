#!/usr/bin/python

# Semaforo
import sys
from socket import *
import time
import threading

# Default server
serverName = '192.168.1.145'
serverPort = 12000

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
        except clientSocket.recv(2048) == "sos":
            green()
        try:
            red()
        except clientSocket.recv(2048) == "sos":
            green()

# Optional server port number
#if (len(sys.argv) > 2):
#	serverPort = int(sys.argv[2])

# Request IPv4 and TCP communication
clientSocket = socket(AF_INET, SOCK_STREAM)

# Open the TCP connection to the server at the specified port
try:
    clientSocket.connect((serverName,serverPort))
except:
    print('No es pot connectar amb el servidor')
    print('Server: '+serverName)
    print('Port: %d' % serverPort)
    exit(-4)

# Read in some text from the user
clientSocket.listen(1)

# Traffic light function
luz = threading.Thread(target=luces)
luz.start()


