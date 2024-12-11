import socketio

sio = socketio.Client()

@sio.event
def connect():
    sio.emit("message", {'content' : "hello" })
    print("Connected")
    
@sio.on('response')
def on_response(data):
    print(data)

@sio.event
def disconnect():
    print("Desconectando del servidor")

if __name__ == "__main__":
    # connect

    sio.connect('http://localhost:8080')
    sio.wait()
