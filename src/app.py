import serial

# Configurar el puerto serial con el puerto COM creado
ser = serial.Serial('/dev/ttyV0', 9600, timeout=1)  # Usar COM7

# Leer datos
while True:
    if ser.in_waiting > 0:
        data = ser.read(1)  # Leer un byte
        print(f'Dato recibido: {data}')

