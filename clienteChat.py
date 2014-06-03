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
    time.sleep(1)

def sinc():
  while True:  
    if not escuchar.is_alive():
      break
    t1 = time.time()
    try:
      ts = server.sincronizar()
    except Exception : 
      continue
    ta =  ts + (time.time() - t1)
    time.sleep(1)


escuchar = Thread(target=recibido)
sincro = Thread(target=sinc)
escuchar.start()
sincro.start()

last_message_id = -1
while True:
  if not escuchar.is_alive():
    break
  try:
    msjs = server.recv(int(last_message_id)+1)
  except Exception:
    continue
  for m in msjs:
    if int(m['id']) > last_message_id:
      last_message_id = int(m['id'])
      print('%s dice: %s' % (m['usuario'], m['texto']))
  time.sleep(1)