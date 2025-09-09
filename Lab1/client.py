import socket

# Client configuration
CLIENT_NAME = "Kushal"
SERVER_HOST = '127.0.0.1'  # Server IP
SERVER_PORT = 5000

def start_client():
    while True:
        try:
            client_number = int(input("Enter an integer (1-100): "))
            if not (1 <= client_number <= 100):
                print("Number must be between 1 and 100.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter an integer.")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Send client name and number
    message = f"{CLIENT_NAME} {client_number}"
    client_socket.sendall(message.encode())

    # Receive server response
    data = client_socket.recv(1024).decode()
    parts = data.rsplit(' ', 1)
    server_name = parts[0]
    server_number = int(parts[1])

    # Display results
    print(f"\nClient Name: {CLIENT_NAME}")
    print(f"Server Name: {server_name}")
    print(f"Client Integer: {client_number}")
    print(f"Server Integer: {server_number}")
    print(f"Sum: {client_number + server_number}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
