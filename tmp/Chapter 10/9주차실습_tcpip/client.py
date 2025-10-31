# client.py
import socket

def connect_to_server(host, port, message=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        if message:
            s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print(f"Response from server ({port}): {data.decode('utf-8')}")

if __name__ == "__main__":
    SERVER_IP = input("서버 IP 입력 (예: 192.168.0.10): ")

    print("\n[1] Time Server (5001)")
    connect_to_server(SERVER_IP, 5001)

    print("\n[2] Echo Server (5002)")
    msg = input("Echo할 메시지를 입력: ")
    connect_to_server(SERVER_IP, 5002, msg)

    print("\n[3] Number Server (5003)")
    connect_to_server(SERVER_IP, 5003)
