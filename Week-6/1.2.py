
# Import socket module
import socket            
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
send_message = input('Enter Message ')
s.send(send_message.encode())
# recieve message
recieved = s.recv(1024).decode()
print(f"Recieved message in upper case:- {recieved}")
# close the connection
s.close()    
     

