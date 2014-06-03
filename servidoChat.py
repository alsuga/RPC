from threading import Thread
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random
import math
import time
class RequestHandler(SimpleXMLRPCRequestHandler):
  rpc_paths = ('/RPC2',)

#a = raw_input("Ingrese la direccion ip: ")
#a = "192.168.60.180"
a = "127.0.0.1"
port = 8000
#port = int(input("Ingrese el puerto: "))

server = SimpleXMLRPCServer((a, port),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

usuarios = []
mensajes = []

actid = -1

class Mensaje(object):
  def __init__(self, mid,user,ms):
    self.id  = mid
    self.usuario = user
    self.texto = ms
    

def log(usuario):
  global usuarios, mensajes, actid
  if usuario in usuarios:
    return True 
  usuarios.append(usuario)
  actid += 1
  msj = Mensaje(actid,"servidor",usuario + " se ha conectado")
  mensajes.append(msj)
  return False

def logout(usuario):
  global usuarios, mensajes, actid
  usuarios.remove(usuario)
  actid += 1
  msj = Mensaje(actid,"servidor",usuario + " se ha desconectado")
  mensajes.append(msj)

def enviado(usuario,tex):
  global actid, mensajes
  actid += 1
  msj = Mensaje(actid,usuario,tex)
  mensajes.append(msj)

def recv(last_id):
  global mensajes
  a = []
  for m in mensajes:
    if int(m.id) >= last_id:
      a.append(m)
  return a

def sincronizar():
  t1 = time.time()
  return t1

server.register_function(log)
server.register_function(logout)
server.register_function(enviado)
server.register_function(recv)
server.register_function(sincronizar)
server.serve_forever()
