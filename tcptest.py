import socket
import zlib
import base64 

# Flux TCP 
HOST = '212.129.38.224'
PORT = 52022
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print('Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.')

def send_datas(msg): # send datas to host + port
  print('Envoi de :' + msg)
  n = client.send(msg)
  if (n != len(message)):
          print('Erreur envoi.')
  else:
          print('Envoi ok.')
          datas = client.recv(1024)
  return datas

def zlib_d(zlib_datas_to_decode): #decompress zlib
  return zlib.decompress(zlib_datas_to_decode)

def base64_d(base64_datas_to_decode): #decompress base64
  return base64.b64decode(base64_datas_to_decode)

# Main 
datas = send_datas(msg = 'Hello, world')
print('Reception...')
print('These datas were receives :' + datas)
datas_d = zlib_d(datas)
datas_d_clear = base64_d(datas_d)
datas = send_datas(datas_d_clear)
print('Datas uncompress :' + datas)
print('Deconnexion.')

client.close()
