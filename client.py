
import random # This generate randomized lost packets.
import time # This will record the time.
import struct
import sys
from socket import *

#//////////////////////////Client Side//////////////////////////////////

argv=sys.argv
IP = argv[1] #localhost 
PORT = argv[2]
BUFFER_SIZE = argv[3]
BUFFER_SIZE = int(BUFFER_SIZE)
PORT = int(PORT)
ping = 1 #start ping
number_received = 0
number_loss = 0
print("Pinging "+ str(IP)+", "+str(PORT))
clientSocket = socket(AF_INET, SOCK_DGRAM) #Create A UDP client socket. We use SOCK_DGRAM for UDP.
clientSocket.settimeout(1)
lst = []
while (ping < 11) :
 
    msg=struct.pack("!i",ping) #Byte ordering in the message
     
    start= time.time()  # record the start time
    
    print("Ping message number "+ str(ping))
 
    
    clientSocket.sendto(msg,(IP,PORT)) #Send message(request) to server.
    time.sleep(1)
 
    try:
        
        receivedMessage, serverAddress = clientSocket.recvfrom(BUFFER_SIZE) #Receive the server response
        receivedMessage= str(receivedMessage)
        serverAddress= str(serverAddress)
        print("Receive data from server")
        end=time.time()
        RTT= ((end) - (start))
        lst.append(RTT)
        print("RTT: " + str(RTT)+ " secs")
        number_received = number_received + 1
    except timeout:
        print("Message time out")
        number_loss = number_loss + 1

    ping = ping + 1

min_RTT= min(lst)
max_RTT= max(lst)
average_RTT= (min_RTT+ max_RTT)/2
print("\n")
print("Number of packets received: " + str(number_received))
print("Number of packets sent: " + str(ping-1))
print("% loss rate: "+ str(number_loss*10) + "%")
print("Min RTT: "+ str(min_RTT))
print("Max RTT: " + str(max_RTT))
print("Average RTT: "+ str(average_RTT))
   
