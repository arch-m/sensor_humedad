# INSTALACION
Instalar y ejecutar virtual enviroment de Python
> python3 -m venv env

Ir a ruta
> cd env/bin

Activar virtual enviroment
> source activate

Instalar paquetes
> pip install pyserial

Se debe multiplexar una terminal o utilizar en su defecto mas de un ventana o metodo
preferido para tener tres procesos en ejecucion

*server.py* se mantiene escuchando al puerto para leer los bits de entrada y enviarlos al socket
que se encuentra configurado en la ruta *http://localhost:8080*, se decide
utilizar durante la fase pruebas los puertos virtuales ttyV0 y ttyV1, por ello, se
requieren permisos de ejecucion de tipo adminstrador (sudo)

*client.py* es un archivo temporal y sera remplazado por un proyecto de React con SocketIO
y su unica funcion actual es mantenerse como cliente de lectura de cadena.

*create_virtual_port* contiene la informacion de como se puede crear un puerto virtual utilizando
el paquete sockt de GNU/Linux para sistemas Windows se recomienda utilzar WSL2 y en su defecto
herramientas como com0com, sin embargo, no ha sido probado bajo este sistema operativo. En MacOSX
se mantiene el soporte a sockt mediante el manejador HomeBrew o MacPorts.

En este mismo archivo se puede encontrar la descripcion para enviar una cadena de prueba al puerto
virtual, se requieren permisos de superadministrador. Utilizar sudo su o alternativa deseada con
precaucion.
