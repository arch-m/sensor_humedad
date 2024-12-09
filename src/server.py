import socket
import serial
import time

# Puerto serial
ser = serial.Serial('/dev/ttyV0', 9600, timeout=1)

# Crear el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligar socket a la ruta y puerto
server_socket.bind(('localhost', 8080))

# Habilitar socket para recibir las conexiones
server_socket.listen(1)

print("Server listening on port 8080...")

# Aceptar las conexiones entrantes
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    if ser.in_waiting > 0:
        data = ser.read(8)
        print(f'Data received {data}')
        # Enviar mensaje al cliente
        client_socket.sendall(data)
        # Dormir 2ms
        time.sleep(0.2)

# Cerrar las conexiones

client_socket.close()
server_socket.close()
