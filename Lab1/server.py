import socket
import random

# Server configuration
SERVER_NAME = "MyServer"
HOST = '127.0.0.1'  # Localhost
PORT = 5000         

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"{SERVER_NAME} listening on {HOST}:{PORT}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        try:
            data = conn.recv(1024).decode()
            if not data:
                conn.close()
                continue

            # Extract client name and number
            parts = data.rsplit(' ', 1)  
            client_name = parts[0]
            client_number = int(parts[1])

            # Check number validity
            if not (1 <= client_number <= 100):
                print("Received invalid number. Terminating server.")
                conn.close()
                server_socket.close()
                return

            # Generate server number
            server_number = random.randint(1, 100)

            # Display info
            print(f"Client Name: {client_name}")
            print(f"Server Name: {SERVER_NAME}")
            print(f"Client Integer: {client_number}")
            print(f"Server Integer: {server_number}")
            print(f"Sum: {client_number + server_number}")

            # Send reply
            reply = f"{SERVER_NAME} {server_number}"
            conn.sendall(reply.encode())

        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    start_server()
