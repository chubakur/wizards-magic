# To change this template, choose Tools | Templates
# and open the template in the editor.
import socket
try:
    import json
except ImportError:
    import simplejson as json
host = "flareguner.zapto.org"
port = 7712
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print "CONNECTED"
def get_package():
    #print "SERVICE:"
    #print service_package
    MSGLEN, answ = int( sock.recv(8) ), ''
    while len(answ)<MSGLEN: answ += sock.recv(MSGLEN - len(answ))
        #return answ
    print "GET_PACKAGE RETURN"
    print answ
    return json.loads(answ)
def query(query):
    query = json.dumps(query)
    service = '%08i'%len(query)
    sock.send(service)
    sock.send(query)
    #print sock.recv(1)
    #return
    #return get_package()

