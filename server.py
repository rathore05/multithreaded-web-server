# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading
import sys
import time

  
# thread fuction 
def threaded(c, i): 
    while True: 

        try:
            # data received from client 
            data = c.recv(1024)
        except Exception as e:
            print("Connection closed with client ", i, ": Further data can't be received....")

            break
         
        if not data: 
            print('Bye') 
               
            break
  
        # send back reversed string to client 
        data = data[::-1] 
        #print(c)
        try:
            c.send(data) 
        except Exception as e:
            print("Connection closed with client ", i, ": Further data can't be send....")

        
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 

    port = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 

    connections = ()
  

    currentConnections = 0
    maxConnections = int(sys.argv[1])
    
    i = 0
    j = 0

    # a forever loop until client wants to exit 
    while True: 
          
        # establish connection with client 
        c, addr = s.accept() 


        #print(c)
        if currentConnections >= maxConnections:
            #print(connections[i])
            connections[i].close()
            print("\n"+"Connection closed with client ", i)
            os_memory_report(i,j)
            i = i + 1

        
        new = connections + (c,)
        #print(new)
        connections = new
        
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c, j)) 
        j = j + 1

        currentConnections = currentConnections + 1

    time.sleep(5)

    s.close() 


def os_memory_report(i, j):
    print("Cleaning up shared state of client", i, "for client", j)
    time.sleep(2)
    print("Cleaned up shared state of client", i, "for client", j)
    time.sleep(2)    

  
if __name__ == '__main__': 
    Main() 

    
