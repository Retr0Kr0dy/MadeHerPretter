import threading, socket, sys


#color console
W = '\033[0m' #white
R = '\033[31m' #red
G = '\033[32m' #green
O = '\033[33m' #orange
B = '\033[34m' #blue
P = '\033[35m' #purple
C = '\033[36m' #cyan
GR = '\033[37m' #grey

try:
    host=sys.argv[1]
except:
    host = input (B+"\nEnter the IP of the host server (or leave empty for localhost) : "+W)
    if len(host) == 0:
        host = '127.0.0.1' 

try:
    port=int(sys.argv[2])
except:
    port = int(input (B+"\nEnter the listening port of the host server : "+W))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients_list = []
address_list = []
con = ''

def listen():
    while True:
        client, address = server.accept()
        print (B+"\nNew user connected at "+G+str(address)+'\n'+W)
        clients_list.append(client)
        address_list.append(address)
        print (clients_list)

thread = threading.Thread(target=listen)
thread.start()

def console(client):
    a = input(P+"HACKER"+B+"_"+O+"@"+B+"_"+P+str(address_list[clients_list.index(client)])+B+"_"+P+"FROM"+B+"_"+P+str(host)+B+"#"+P+"¬ "+W) 
    if 'QUIT' in a:
        main()
    if 'DISCONNECT' in a:
        a = bytearray(a.encode('utf-8')) 
        client.send(a)
        print (R+"\nDisconnected at "+G+str(address_list[clients_list.index(client)])+'\n'+W)
        clients_list.remove(client)
        main()
    a = bytearray(a.encode('utf-8')) 
    client.send(a)
    reciv(client)
    console(client)

def broadcast(message):
    for client in clients_list:
        index=clients_list.index(client)
        print(B+"\n    ["+P+str(index)+B+"]"+O+" - "+G+"AA"+O+" - "+P+str(client)+"\n")
        client.send(message)

def brdcst():
    a = input(P+"HACKER"+B+"_"+O+"@"+B+"_"+P+"NODE1"+B+"_"+P+"FROM"+B+"_"+P+host+B+"#"+P+"¬"+W) 
    if 'QUIT' in a:
        main()
    if 'DISCONNECT' in a:
        a = bytearray(a.encode('utf-8'))
        for client in clients_list:
            print (B+"\n    ["+P+str(clients_list.index(client))+B+"] - "+P+str(address_list[clients_list.index(client)])+W)
        client = clients_list[int(input(B+"\n  client index :"+W))] 
        print()     
        client.send(a)
        print (R+"\nDisconnected at "+G+str(address_list[clients_list.index(client)])+'\n'+W)
        clients_list.remove(client)
        main()
    if len(a) == 0:
        brdcst()
    a = bytearray(a.encode('utf-8')) 
    broadcast(a)
    brdcst()

def reciv(client):
    message = client.recv(2048)
    message = message.decode()
    print (message)

def main():
    while True:
        a = input(P+"HACKER"+B+"_"+O+"@"+B+"_"+P+host+B+"#"+P+"¬"+W) 
        if "QUIT" in a:
            print (R+"\nQUITTING...")
            quit()
            exit(-1)
        if "CONSOLE" in a:
            def ask():
                try:
                    for client in clients_list:
                        print (B+"\n    ["+P+str(clients_list.index(client))+B+"] - "+P+str(address_list[clients_list.index(client)])+W)
                    client = clients_list[int(input(B+"\n  client index :"+W))] 
                except:
                    ask()
            print()
            console(client)
        if "CLIENT" in a:
            print (B+"\nCLIENT_LIST\n")
            for client in clients_list:
                print (B+"\n    ["+P+str(clients_list.index(client))+B+"] - "+P+str(address_list[clients_list.index(client)])+W)
        if "BROADCAST" in a:
            brdcst()
        if a == 'DISCONNECT':
            a = bytearray(a.encode('utf-8'))
            for client in clients_list:
                print (B+"\n    ["+P+str(clients_list.index(client))+B+"] - "+P+str(address_list[clients_list.index(client)])+W)
            client = clients_list[int(input(B+"\n  client index :"+W))] 
            print()     
            client.send(a)
            print (R+"\nDisconnected at "+G+str(address_list[clients_list.index(client)])+'\n'+W)
            clients_list.remove(client)
            main()
        if 'DISCONNECT_ALL' in a:
            a = bytearray('DISCONNECT'.encode('utf-8'))
            for client in clients_list:
                client.send(a)
                print (R+"\nDisconnected at "+G+str(address_list[clients_list.index(client)])+'\n'+W)
                clients_list.remove(client)
            main()      
        if len(a) == 0:
            main()
        else:
            print("\nyr mom gay\n")
            main()


print (B+'\nServer is running on '+O+host+B+' using port '+O+str(port)+B+'...\n'+W)


main()

#version 1.0
