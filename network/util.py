from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from socket import gethostbyname
from sys import exit


def createsocket():
    '''
       Python function to create to socket object

       Argument :   None
       Return   :   socket object with of AF_INET family with stream as SOCK_STREAM

    '''
    try:
        #print('Creating socket')
        return socket(AF_INET, SOCK_STREAM)
    except:
        print("Socket cannot be created")
        return Null

def closesocket(name):
    '''
       Python function to close socket connection
       
       Argument : 
                  name: Name of socket object
       Return   : None

    '''
    try:
        #print('Closing socket')
        name.close()
    except:
        print("Socket cannot be close")
    
    
def setupconnection(name,host,port): 
    '''
       Python function to setup the connection to a port on a host
   
       Argument  : 
                   name: Name of socket object
                   host: Host where we need to connect
                   port: Port where we need to connect

       Return    : None on failure, otherwise True.
    '''

    if not isinstance(name,socket):
        print('socket object should be passed')
        closesocket(name)
        return None

    try: 
        gethostbyname(host)
    except:
        print('Host Name is not reachable')
        closesocket(name)
        return None
        
    if not isinstance(port,int):
        print("Port number should be integer")
        closesocket(name)
        return None

    try:
        name.connect((host,port))
        return True
    except:
        #print('Connection Refused')
        closesocket(name)
        return None

