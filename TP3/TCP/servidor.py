import socket, subprocess
import sys
from thread import *

CROJO = '\033[91m'
CVERDE = '\033[92m'
CCYAN = '\033[96m'
CDE = '\033[0m'
 
HOST = subprocess.check_output("hostname -I | awk '{ print $1}'", shell=True)   # Numero de Host
HOST = HOST[:-1] 
PORT = 1234 # Numero de Puerto

BUFFER_SIZE =  1024
 
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket TCP creado'

#Asocia el puerto al socket
try:
    ss.bind((HOST, PORT))
except socket.error as msg:
    print 'Fallo en bind. Codigo de error : ' + str(msg[0]) + ' Mensaje ' + msg[1]
    sys.exit()
     
print 'Socket bind exitoso'
 
#Escucha de socket servidor. Cantidad maxima de conexiones '2'
ss.listen(2)
print "Servidor escuchando en" + CCYAN + " %s" %str(ss.getsockname()) + CDE
 
#Funcion de creacion de hilos para asociarlos a cada conexion entrante.
def clientthread(sc):
    #Enviendo mensaje de bivenida al cliente recien conectado
    sc.send("Bienvenido al servidor %s.\nEscribe un mensaje y preciona Enter. ('q' para finalizar sesion)" %str(ss.getsockname()))
     
    #Bucle de conexion con el cliente.
    while True:
         
        #Recibiendo mensaje del cliente
        mensaje = sc.recv(BUFFER_SIZE)
        mensaje = mensaje[:-1]
        if(mensaje == "q"):
        	sc.send("Fin de sesion")
        	break	
        print "Mensaje recibido de %s: %s" %(str(sc.getpeername()),mensaje)
        replica = 'OK...' + mensaje    
        sc.send(replica)
     
    #Salir del bucle
    print (CROJO + "Conexion finalizada con %s" %str(sc.getpeername()) + CDE)
    sc.close()
 
#Bucle a la espera de conexiones entrantes - LLamada bloqueante
while 1:
	#ss.listen(2)
	sc, addr = ss.accept()
	print (CVERDE + 'Conectado con %s' %str(sc.getpeername()) + CDE)
	#Comenzar nuevo hilo asociado al cliente
	start_new_thread(clientthread ,(sc,))

ss.close()
