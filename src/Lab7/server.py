import socket
from smtplib import SMTP

HOST = '127.0.0.1'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode()
                i = data.find(" ")
                mass = [data[:i], data[i + 1:]]

                with SMTP("smtp.gmail.com:587") as smtp:
                    smtp.starttls()
                    smtp.sendmail("Hello@gmail.com", mass[0], mass[1])

                if not data:
                    break
                conn.sendall(b"Ok")
