import socket
import serial
import time

# Serial port
ser = serial.Serial('/dev/ttyV0', 9600, timeout=1)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('localhost', 8080))

# Enable the server to accept connections (max 5 clients in the queue)
server_socket.listen(1)

print("Server listening on port 8080...")

# Accept incoming client connections
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    if ser.in_waiting > 0:
        data = ser.read(8)
        print(f'Data received {data}')
        # Send a message to the client
        client_socket.sendall(data)
        time.sleep(0.2)

    # Close the client connection

client_socket.close()
server_socket.close()
