import sys
import socket
from asses import send_file,recv_file,list_directory


srv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


try:
    srv_sock.bind(("0.0.0.0", int(sys.argv[1])))  #1st on cmd line
    srv_sock.listen(5)
    print("server up and running ")
except Exception as e:
    print(e)
    exit(1)

while True:
    try:
        print("waiting for client")
        cli_sock, cli_addr = srv_sock.accept()
        cli_addr_str = str(cli_addr)
        print("client " + cli_addr_str + " connected")

        commandrecv = cli_sock.recv(1024)
        command = commandrecv.decode('utf-8')
        commandsplit = command.split(",")
        filename = commandsplit[1]
        

        if commandsplit[0]=="get":
             print(f"Download request from client for {filename} ")
             send_file(cli_sock,filename)
        if commandsplit[0]=="put":
             print(f"Upload request from client for {filename}")
             recv_file(cli_sock, filename)
        if command=="list":
             print("Directory Listing request from client")
             list_directory(cli_sock)
    except ConnectionResetError as e:
         print("Client closed connection")
        
    finally:
         cli_sock.close()

srv_sock.close()

exit(0)






