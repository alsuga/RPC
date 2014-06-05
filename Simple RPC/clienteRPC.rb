require "xmlrpc/client"
require 'socket'
#a = Socket.ip_address_list.detect{|intf| intf.ipv4_private?}.getnameinfo[0]
a = "192.168.60.180"

server = XMLRPC::Client.new(a, "/RPC2", 8000)

puts "Ingrese un numero: "
a = gets.chomp.to_i
ok, param = server.call2("Primo?", a)
if ok then
  puts "es primo? #{param}"
else
  puts "Error:"
  puts param.faultCode
  puts param.faultString
end