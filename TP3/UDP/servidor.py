
import socket, subprocess

CROJO = '\033[91m'
CVERDE = '\033[92m'
CCYAN = '\033[96m'
CDE = '\033[0m'

HOST = subprocess.check_output("hostname -I | awk '{ print $1}'", shell=True)   # Numero de Host
HOST = HOST[:-1] 
PORT = 1234 # Numero de 
BUFFER_SIZE =  1024

# Creacion del socket
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Socket UDP creado' 
# Asignacion del numero de puerto al socket
try:
    ss.bind((HOST, PORT))
except socket.error as msg:
    print 'Fallo en bind. Codigo de error : ' + str(msg[0]) + ' Mensaje ' + msg[1]
    sys.exit()
     
print 'Socket bind exitoso'
 
print "Servidor escuchando en" + CCYAN + " %s" %str(ss.getsockname()) + CDE

while 1:
    # Recepcion de datos del cliente (data, addr)
    d = ss.recvfrom(BUFFER_SIZE)
    data = d[0]
    addr = d[1]
         
    respuesta = 'OK...' + data
    # Envio de mensaje de respuesta al cliente (replica) 
    ss.sendto(respuesta , addr)
    print 'Mensaje recibido de ('+addr[0]+','+ str(addr[1])+'): ' + data.strip()
     
ss.close()
