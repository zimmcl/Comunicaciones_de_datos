import socket, sys, os, subprocess
import random

UDP_IP = str(sys.argv[1])
UDP_PORT = int(sys.argv[2])
BUFFER_SIZE = 1024

CROJO = '\x1b[1;31m'
CVERDE = '\x1b[1;32m'
CCYAN = '\x1b[1;36m'
CAMA = '\x1b[1;33m'
CDE = '\033[0m'

CLIENT_HOST = subprocess.check_output("hostname -I | awk '{ print $1}'", shell=True)
CLIENT_PORT = random.randint(1250, 54100)

# Creacion del socket
sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Asignacion del numero de puerto al socket
sc.bind((CLIENT_HOST, CLIENT_PORT))
if(sc!=-1):
	print "Socket instanciado %s" %str(sc.getsockname())
	print "Conexion establecida con (%s,'%s')" %(UDP_IP,UDP_PORT) + " - (q) para salir"
else:
	print "No se pudo establecer conexion con (%s,'%s')" %(UDP_IP,UDP_PORT)
	sys.exit(1)

while (1):
	sys.stdout.write("Mensaje-> ")
	mensaje = sys.stdin.readline()
	mensaje = mensaje[:-1]
	if mensaje=='q':
		break
	else:
		# Envio de mensaje al servidor (data, addr)
		sc.sendto(mensaje, (UDP_IP, UDP_PORT))
		# Recepcion de mensaje de respuesta del servidor
		data = sc.recvfrom(BUFFER_SIZE)
		print "Respuesta: %s " %(data[0])
sc.close()