import socket
from _thread import *
import sys
server = "10.74.23.113"

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
playerList = []

try:
    s.bind((server, port))

except socket.error as e:
    str(e)


    


s.listen(2)

print("waiting for a connection, server started")

def threaded_client(conn, player):
    
    if player % 2 == 0:
        conn.send(str.encode(str(2)))
    else:
        conn.send(str.encode(str(1)))
    print(player)
    reply = ""
    while True:
        
        try:
            data = conn.recv(2040).decode()
            
            if not data:
                print("disconnected")
                break
            else:    
                if player%2 == 1:  
                    while len(playerList) <= player:
                        #nothing
                        cat = ''

                    reply = data
                    print(data)
                    print(playerList[player])                
                                
                    playerList[player].send(str.encode(reply))
                         


                else:
                    reply = data
                    print(data)
                    print(playerList[player-2])
                    playerList[player-2].send(str.encode(reply))
        except:
            break
    print("Lost Connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    playerList.append(conn)
    print("connected to", addr)
    currentPlayer += 1
    start_new_thread(threaded_client, (conn, currentPlayer))
    
    