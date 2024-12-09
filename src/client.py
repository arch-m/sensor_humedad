import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (replace 'localhost' with server's IP if needed)
client_socket.connect(('localhost', 8080))

while True:
    # Receive the response from the server
    response = client_socket.recv(1024)

    if not response:
        print("no")
        break

    print(f"Received from server: {response.decode()}")

# Close the connection
client_socket.close()
