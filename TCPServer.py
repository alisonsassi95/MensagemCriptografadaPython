from socket import *
import sys


serverPort = 13000
# Create socket using the given port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
pos = 13

def Cripto(clientSentence, dir):
    m = ''
    for c in clientSentence:
        if c in alphabet:
            c_index = alphabet.index(c)
            m += alphabet[(c_index + (dir * pos)) % len(alphabet)]
        else:
            m += c
    return m

print 'Listening on port', serverPort, '...'
# While loop to handle arbitrary sequence of clients making requests
while 1:
    # Waits for some client to connect and creates new socket for  connection
    connectionSocket, addr = serverSocket.accept()
    print 'Client Made Connection', addr 
    # Read input line from socket
    clientSentence = connectionSocket.recv(1024)
    #calls the crypto method and passes the message with the delete    position
    clientSentence = Cripto(clientSentence, -1)


    print 'FROM CLIENT:', clientSentence
   # Capitalize the sentence
    serverSentence = clientSentence.upper()
    # Write output line to socket
    connectionSocket.send(serverSentence)
    print 'TO CLIENT', serverSentence
    # Close the connection socket
    connectionSocket.close()
