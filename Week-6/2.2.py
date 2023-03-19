# Import socket module
import socket
import random            

auth = True

while auth == True:
    ip = str(random.randint(2, 99))
    ipnet = '127.0.0.'+ ip
    # Create a socket object
    s = socket.socket()        
    
    # Define the port on which you want to connect
    port = 12345               
    
    # connect to the server on local computer
    s.connect((ipnet, port))
    
    # receive data from the server and decoding to get the string.

    send_message = input('Enter Message:- ')
    s.send(send_message.encode())
    # recieve message
    recieved = s.recv(1024).decode()
    print(recieved)
    
    # close the connection
    s.close()    
     


