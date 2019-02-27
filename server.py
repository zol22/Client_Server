################################################################
#   Name: Solange Ormeno                                       #
#   UCID: so228                                                #                                
#   Section: CS 356- 006                                       #
################################################################


import random # This generate randomized lost packets.
import time # This will record the time.
import struct,sys
from socket import *

argv=sys.argv
IP = argv[1] #localhost 
PORT = argv[2]
BUFFER_SIZE = argv[3]
BUFFER_SIZE = int(BUFFER_SIZE)
PORT = int(PORT)



#////////////////////////////Server Side///////////////////////////////
serverSocket = socket(AF_INET,SOCK_DGRAM) # Create a UDP socket

serverSocket.bind((IP,PORT)) #Assign IP address and port number to socket
print("The server is ready to receive on port:" + str(PORT))

#loop forever listening for incoming datagram message.
while True:
    rand = random.randint(0,10) #Generate random number in the range of 0 to 10


    time.sleep(1)
    msg,addr = serverSocket.recvfrom(BUFFER_SIZE) #Receive request from client along with the address it is coming from.
    message=struct.unpack("!i",msg)
    message=str(message)
    print("Responding to ping request with sequence nummber"+message)
 
    
    # If rand is less than 4, the packet is lost , Therefore, server doesnt respond.
    if rand < 4:
        print("Message with sequence number"+ message + "dropped")
        continue
        
    
    #Otherwise,if rand is greater than 4, the server responds
    print("Sending data to client")
    serverSocket.sendto(message.encode(),addr)  #send response to client
pass
