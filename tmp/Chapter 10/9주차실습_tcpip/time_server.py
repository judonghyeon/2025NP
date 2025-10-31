# time_server.py
import socket
import datetime

HOST = '0.0.0.0'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[Time Server] Listening on port {PORT}...")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn.sendall(current_time.encode('utf-8'))
