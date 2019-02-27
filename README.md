# UDP Ping Client and Server

Using UDP sockets,  this client and server program enables the client to determine the round-trip time (RTT) 
to the server. To determine the RTT delay, the client records the time on sending a ping request to the server, and then 
records the time on receiving a ping response from the server.  
The difference in the two times is the RTT. 

## GETTING STARTED

### Prerequisites

install python3 in your computer

### Installing

MAC:  
1.  ```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" ```
2.	```	brew doctor	```
3.	```	brew install python3 ```


## RUNNING THE TEST

### Parameters

The client program take the following input parameters:

- ```IP address```

- ```IP port ```

- ```Buffer size```

The client program will read in the above input parameters, and send 10 ping requests consecutively, waiting 
for a response each time, to the server running at the specified IP address and port. After each response is 
received, the client calculates and prints the RTT for the message.

### Run

Client: ```python3 client.py 127.0.0.1 12000 1024      ```

Server: ```python3 client.py 127.0.0.1 12000 1024      ```
