import xmlrpclib

#a = raw_input("Ingrese la direccion ip del servidor: ")
#port = raw_input("Ingrese el puerto del puerto del servidor: ")
a = "192.168.60.180"
#a = "127.0.0.1"
port = "8000"
where = "http://"+a+":"+port

s = xmlrpclib.ServerProxy(where)
print "hola, vamos a jugar, se gana 2 de 3"

l = s.system.listMethods()
num = 1
for i in l:
  if "system" in i:
    continue
  print str(num) + " " + i
  num +=1

a = int(input())
win = 0
lose = 0
if a == 2:
  print "1 Piedra, 2 Papel, 3 Tijeras:"
  while win <= 1 and  lose <= 1:
    a = int(input())
    b =  s.PiedraPapelOTijera(a)
    if b == 2:
      print "Todo un genio malvado"
      continue
    if b == 0:
      print "Empato"
    if b == -1:
      lose += 1
      print "Perdio!"
    if b == 1:
      win += 1
      print "Gano!"
elif a == 1:
  print "Adivine el numero mas cercano, ingrese uno del 1 al 10:"
  while win <= 1 and  lose <= 1:
    a = int(input())
    b =  s.CercaDelNumero(a)
    if b[0] == "G":
      win += 1
    elif b[0] == "P":
      lose += 1
    print b


if win != 0 or lose != 0:
  print "Resultado final: "
if win == 2:
  print "Gano"
elif lose == 2:
  print "Perdio"
  