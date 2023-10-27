import sys
import socket
import os


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
                if not file_data:
                    raise Exception("File is empty")
            socket.sendall(file_data)
            print(f"File {filename} sent successfully")
        except Exception as e:
            print(f"error {e}")


                