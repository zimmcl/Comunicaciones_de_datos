import socket
import sys, select, os
from time import time, sleep
  
sys.stdout.write("Sistema de conexion TCP\n") 
sys.stdout.write("Ingrese el numero de host del servidor: ")
sys.stdout.flush()
HOST = sys.stdin.readline() 
PORT = input("Ingrese el numero de puerto del servidor: ")

CROJO = '\x1b[1;31m'
CVERDE = '\x1b[1;32m'
CCYAN = '\x1b[1;36m'
CAMA = '\x1b[1;33m'
CDE = '\033[0m'
color = ""

# Funcion de barra de progreso
def update_progress(titulo, progreso):
    length = 30 # Longitud de la barra de progreso
    block = int(round(length*progreso))
    if block <=10:
    	color = CVERDE
    if block <=22 and block>10:
    	color = CAMA
    if block >22:
    	color = CROJO
    msg = "\r{0}: [{1}] {2}seg Mensaje->> ".format(titulo, color+"#"*(block-length) + "#"*(length-block)+CDE,30-tiempo)
    if progreso >= 1:
    	#msg += "FIN SESION\r\n"
    	msg = "\r{0}: [{1}]\n".format(titulo, color+"SESION FINALIZADA POR INACTIVIDAD"+CDE)
    sys.stdout.write(msg)
    sys.stdout.flush()

BUFFER_SIZE = 1024
tiempo = 0
lastShownPercent = 0
 
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sc.connect((HOST, PORT))
except socket.error, msg:
	print "No se pudo establecer la conexion con el servidor ('%s', %s).\nPrograma finalizado" %(HOST, PORT)
	sys.exit(1)

print "Socket creado " + CCYAN + "%s" %str(sc.getsockname()) + CDE
mensaje = sc.recv(BUFFER_SIZE)
print mensaje
while tiempo<30:
	if (not select.select([sys.stdin,],[],[],0.0)[0]):
		sleep(1)
		tiempo += 1
		percentComplete = int(round(( float(tiempo) / 30) * 100))
		if (lastShownPercent != percentComplete):
			lastShownPercent = percentComplete
			update_progress("Inactividad", percentComplete/100.0)
	
	else:
		sys.stdout.flush()
		MENSAJE = sys.stdin.readline()
		sc.send(MENSAJE)
		os.system('cls' if os.name == 'nt' else 'clear')
		mensaje = sc.recv(BUFFER_SIZE)
		if mensaje!='Fin de sesion':
			print "Bienvenido al servidor %s.\nEscribe un mensaje y preciona Enter. ('q' para finalizar sesion)" %str(sc.getpeername())		
		print mensaje
		tiempo = 0
		if mensaje == "Fin de sesion":
			print CVERDE + "SESION FINALIZADA POR EL USUARIO" +CDE
			break

if(tiempo==30 and mensaje!='q'):
	sc.send("q ")
	sc.recv(BUFFER_SIZE)
	#print CROJO + "Sesion finalizada por inactividad" +CDE
sc.close()
