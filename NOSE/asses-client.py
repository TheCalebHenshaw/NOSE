import socket
import sys


cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srv_addr = (sys.argv[1], int(sys.argv[2]))

srv_addr_str = str(srv_addr)


try:
    print("Connecting to " + srv_addr_str + " ....")
    cli_sock.connect(srv_addr)
    print("Now connected")
except Exception as e:
    print(e)
    exit(1)
