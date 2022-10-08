import socket

HOST = '127.0.0.1'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    email = input("Enter Email: ")
    message = input("Enter your message: ")
    s.sendall((email + " " + message).encode())
    data = s.recv(1024)
print('Received', repr(data.decode()))
