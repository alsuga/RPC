require "xmlrpc/server"
require 'prime'
require 'socket'
#a = Socket.ip_address_list.detect{|intf| intf.ipv4_private?}.getnameinfo[0]
a = "192.168.60.180"
s = XMLRPC::Server.new(8000,a)
s.add_handler("Primo?") do |a|
  Prime.prime?(a)
end

s.set_default_handler do |name, *args|
  raise XMLRPC::FaultException.new(-99, "Method #{name} missing" +
                                   " or wrong number of parameters!")
end

s.serve
