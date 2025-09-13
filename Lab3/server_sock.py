import socket
import random
import time

def handle_client(client_socket):

    request = client_socket.recv(1024).decode()
    

    lines = request.split('\r\n')
    method, path, _ = lines[0].split()
    

    cookie = None
    for line in lines:
        if line.startswith('Cookie:'):
            cookie = line.split(':')[1].strip()
            break
    

    if not cookie:
        session_id = f"User{random.randint(1000, 9999)}"
        response = (
            "HTTP/1.1 200 OK\r\n"
            f"Set-Cookie: session={session_id}; HttpOnly\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            f"<html><body><h1>Welcome! Your session ID is {session_id}</h1></body></html>"
        )
    else:

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            f"<html><body><h1>Welcome back! Your session ID is {cookie}</h1></body></html>"
        )
    

    client_socket.send(response.encode())
    

    client_socket.close()

def start_server(host='0.0.0.0', port=8081):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"Server running on http://{host}:{port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server(port=8081)

