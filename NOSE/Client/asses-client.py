import socket
import sys
from asses import send_file,recv_file,recv_directory

if sys.argv[3]!="list":
    command = sys.argv[3]+","+sys.argv[4]
else:
    command = sys.argv[3]

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

try:
    cli_sock.send(command.encode())
    if sys.argv[3]=="get": #download
        print(f"downloading file {sys.argv[4]} ...")
        recv_file(cli_sock,filename)
    if sys.argv[3]=="put": #upload
        print(f"uploading file {sys.argv[4]} ...")
        send_file(cli_sock,filename)
    if sys.argv[3]=="list": #list the directory
        recv_directory(cli_sock)
    
except Exception as e:
    print(f"Error {e}")
        


cli_sock.close()

exit(0)
