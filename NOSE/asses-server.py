import sys
import socket


srv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



try:
    srv_sock.bind(("0.0.0.0:",int(sys.argv[1])))  #1st on cmd line
    srv_sock.listen(5)
    print(srv_sock.accept()+" Success")
except Exception as e:
    print(e)
    exit(1)


