import time
import socketio
import eventlet
eventlet.monkey_patch()
import serial

# Voltaje de resolucion
vres = 0.0619

# Puerto definicion
portRoute = '/dev/ttyV0'
port = 9600

# Puerto serial
ser = serial.Serial(portRoute, port, timeout=1)

# Crear el socket
sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)

# Evento de conexion
@sio.event
def connect(sid, environ):
    print(sid)
    sio.emit("respuesta", {"nombre": "Hello"}, to=sid)

def start_stream():
    print("Leyendo puerto...")
    while True:
        if ser.in_waiting > 0:
            data = ser.read(8)
            print(data)
            vsensor = round(int(data.decode('utf-8'), 2) * vres, 4)
            sio.emit("resonga", {"nombre": vsensor })

        eventlet.sleep(0.2)

# Evento personalizado
@sio.event
def mensaje(sid, data):
    print(data)
    sio.emit("respuesta", "Servidor recibio", to=sid)

# Desconexion
@sio.event
def disconnect(sid):
    print("desconexion")

if __name__ == "__main__":
    print("Server listening on port 8080...")
    eventlet.spawn(start_stream)
    eventlet.wsgi.server(eventlet.listen(("0.0.0.0", 8080)), app)
