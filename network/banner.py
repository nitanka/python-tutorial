from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from socket import gethostbyname
from sys import exit
from util import *

def grab(host,port):

    '''
       Function to grab the banner of a port

       Arguments:
           socketobject: A socket object which is already connected
           port: The port to which we want to connect
    '''

    socketobject = createsocket()

    if not setupconnection(socketobject,host,port):
        print('Connection Failure')
        return
    
    try:
        if port == 80:
            socketobject.send(b"Get HTTP/1.1 \r\n")
#            print('Packet sent')
        else:
            socketobject.send(b"\r\n")

        results = socketobject.recv(4096)
#        print('Result received')
       
        print('Banner : ' + results.decode())
 

    except: 
        print("Banner not available")
        
    finally:
#        print('Closing socket')
        closesocket(socketobject)    
