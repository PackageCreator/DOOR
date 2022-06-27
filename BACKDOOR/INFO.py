import socket
import time
import threading
host = socket.gethostname()
ip = socket.gethostbyname(host)
sock = socket.socket()
def CONNECT(ipaddress, port):
    try:
        sock.connect((ipaddress, port))
# checks if target has SSH
        ssh_has = True  
    except Exception as e:
        print(e)
        ssh_has = False
    print(ssh_has)
CONNECT("0.0.0.0", 22)
