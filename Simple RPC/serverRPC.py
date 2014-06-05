from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random
import math
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

#a = raw_input("Ingrese la direccion ip: ")
a = "192.168.60.180"
#a = "127.0.0.1"
port = 8000
#port = int(input("Ingrese el puerto: "))

server = SimpleXMLRPCServer((a, port),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

def check(a):
  if a == 1 or a == 2 or a == 3:
    return True
  else:
    return False

def juego1(a):
  if not (check(a)):
    return 2
  b = random.randint(1,3)
  if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b ==1):
    return -1
  elif(a == b):
    return 0
  else:
    return 1

def juego2(a):
  if a < 1 and a > 10:
    return -1
  b = random.randint(1,10)
  jb = random.randint(1,10)
  out = "con "+ str(a) + " contra " +str(b) + " cerca del numero " + str(jb)
  if abs(a - b) < abs(jb - b):
    return "Gano " + out
  elif abs(a - b) > abs(jb - b):
    return "Perdio " + out
  else:
    return "Empato " + out

server.register_function(juego1,"PiedraPapelOTijera")
server.register_function(juego2,"CercaDelNumero")