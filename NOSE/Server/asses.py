import sys
import socket
import os

def socket_to_screen(socket, sock_addr):
    print(sock_addr + ":", end="", flush = True)
    data = bytearray(1)
    bytes_read = 0

    while len(data) > 0 and "\n" not in data.decode():
        data = socket.recv(4096)
        print(data.decode(), end="")
        bytes_read +=len(data)
    return bytes_read


def keyboard_to_socket(socket):
    print( "You: ",end="",flush=True)
    user_input = sys.stdin.readline()
    if user_input=="exit\n":
        return 0


    bytes_sent = socket.sendall(str.encode(user_input))
    return bytes_sent


def list_directory(socket):
    directory = str(os.listdir())
    socket.send(directory.encode())

def recv_directory(socket):
    directory = str(socket.recv(1024).decode())
    print(f"Directory: {directory}")


def recv_file(socket,filename):
    if os.path.exists(filename):
        print(f"{filename} already exists. File not received.")
    if not os.path.exists(filename): #file does not exist
        try:
            file_data = b""
            while True:
                data = socket.recv(1024)
                if not data:
                    break
                file_data +=data
            with open(filename, 'wb') as file:
                file.write(file_data)
            print(f"file {filename} received.")
        except Exception as e:
            print(f"an error has occured: {e}")


def send_file(socket,filename):
        try:
            with open(filename,'rb') as file:
                file_data = file.read()
            socket.sendall(file_data)
            print(f"File {filename} sent successfully")
        except Exception as e:
            print(f"error {e}")


                