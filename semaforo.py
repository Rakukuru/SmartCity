# Cliente de semaforo
import sys
from socket import *

# Default server
serverName = '192.168.1.145'
serverPort = 12000

# Optional server port number
if (len(sys.argv) > 2):
	serverPort = int(sys.argv[2])

# Request IPv4 and TCP communication
clientSocket = socket(AF_INET, SOCK_STREAM)

# Open the TCP connection to the server at the specified port
clientSocket.connect((serverName,serverPort))

# Read in some text from the user
sentence = input('Input lowercase sentence:')

# Send the text and then wait for a response
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(2048)

# Print the converted text and then close the socket
print("From Server: ", modifiedSentence)
clientSocket.close()

