import xmlrpclib
from threading import Thread
import time

#a = raw_input("Ingrese la direccion ip del servidor: ")
#port = raw_input("Ingrese el puerto del puerto del servidor: ")
#a = "192.168.60.180"
a = "127.0.0.1"
whserver = "http://"+a+":"+"8000"

server = xmlrpclib.ServerProxy(whserver)

while True:
  usuario = raw_input('ingrese usuario: ')
  if server.log(usuario):
    print 'usuario en uso'
  else:
    break

def recibido():
  while True:
    tex = raw_input(">> ")
    if tex == '/exit':
      try:
        server.logout(usuario)
      except Exception, e:
        pass
      break
    try:
      server.enviado(usuario,tex)
    except Exception, e:
      pass

def sinc():
  while True:
    t1 = time.time()
    ta = server.sincronizar() + time.time() - t1
    print "hacer algo con la hora " + ta
    time.sleep(1)


escuchar = Thread(target=recibido)
sincro = Thread(target=sinc)
sincro.start()
escuchar.start()


last_message_id = -1
while True:
  if not escuchar.is_alive():
    break
  msjs = server.recv(int(last_message_id)+1)
  for m in msjs:
    if int(m['id']) > last_message_id:
      last_message_id = int(m['id'])
      print('%s dice: %s' % (m['usuario'], m['texto']))
  time.sleep(1)