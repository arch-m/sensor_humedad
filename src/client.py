import socket

# Crear socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al server
client_socket.connect(('localhost', 8080))

while True:
    # Recibir respuesta desde el servidor
    response = client_socket.recv(1024)

    if not response:
        print("no")
        break

    print(f"Received from server: {response.decode()}")

# Cerrar conexion hacia el socket
client_socket.close()


