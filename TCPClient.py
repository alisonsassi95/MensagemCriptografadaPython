from socket import *
import sys

serverName = "localhost"
serverPort = 13000
# Create socket and connect to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# Read line from user
clientSentence = raw_input('Client ready for input\n')
# Write line to server
clientSentence.lower()
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

#calls the cripto method and passes the message with the additional position
clientSentence = Cripto(clientSentence, 1)

clientSocket.send(clientSentence)
print 'TO SERVER:', clientSentence
# Read line from server
modifiedSentence = clientSocket.recv(1024)
print 'FROM SERVER:', modifiedSentence
# Close the socket
clientSocket.close()
