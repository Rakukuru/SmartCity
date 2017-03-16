
from socket import *
import sys



# Default port number server will listen on
#serverName = '192.168.60.238'
serverName = '127.0.0.1'
serverPort = 5005

# Optional server port number
#if (len(sys.argv) > 1):
#	serverPort = int(sys.argv[1])

# Request IPv4 and TCP communication
serverSocket = socket(AF_INET,SOCK_STREAM)

# Open the TCP connection to the server at the specified port

try:
    serverSocket.connect((serverName, serverPort))
except:
    print('No es pot connectar amb el servidor')
    print('Server: '+serverName)
    print('Port: %d' % serverPort)
    exit(-4)

message = "sos"

# Send emergency message
while 1:
	enter = input('Enter command: ')
	if (enter == 'sos'):
		serverSocket.send(b'message')
	if (enter == 'exit'):
		exit(-4)

# Close down the client's socket, not the welcome port
serverSocket.close()
