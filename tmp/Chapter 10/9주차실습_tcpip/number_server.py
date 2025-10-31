# number_server.py
import socket
import random

HOST = '0.0.0.0'
PORT = 5003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[Number Server] Listening on port {PORT}...")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            random_number = str(random.randint(1, 100))
            conn.sendall(random_number.encode('utf-8'))
