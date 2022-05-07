from http import client
import socket, sys

W = '\033[0m'
G = '\033[32m' 
B = '\033[34m' 
P = '\033[35m' 
C = '\033[36m' 

target = sys.argv[1]
port = int(sys.argv[2])

while True:
    msg = str.encode(input(B+"["+G+f"{target}"+B+":"+G+f"{port}"+B+"]"+P+" -["+C+"#"+P+"]- "+W))
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.sendto(msg, (target, port))
    data, addr = c.recvfrom(4096)
    print ("\n" + data.decode())
