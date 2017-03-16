
from socket import *
import sys
import random


# Default port number server will listen on
serverPort = 12000

# Optional server port number
if (len(sys.argv) > 1):
	serverPort = int(sys.argv[1])

# Request IPv4 and TCP communication
serverSocket = socket(AF_INET,SOCK_STREAM)

# The welcoming port that clients first use to connect
serverSocket.bind(('',serverPort))

# Send emergency message

while message = raw_input();
	if (message == 'sos')
		connectionSocket.send(message)

# Close down the client's socket, not the welcome port
connectionSocket.close()
