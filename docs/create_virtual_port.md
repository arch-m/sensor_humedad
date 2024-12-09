Este archivo puede ser transformado a un script de bash para evitar procesos, sin embargo, en la
actualidad describe el como crear e interactuar con un puerto virtual

# Crear un puerto virtual de lectura y escritura

> sudo socat PTY,link=/dev/ttyV0,raw,echo=0 PTY,link=/dev/ttyV1,raw,echo=0

# Enviar cadena puerto

> sudo su
> echo -n "00001111" > /dev/ttyV1
