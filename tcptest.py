import socket

# Flux TCP 
HOST = 'x.x.x.x'
PORT = xxx
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
send_datas(msg = 'Hello, world')
print('Reception...')

donnees = client.recv(1024)
print('Recu :', datas)

def zlib_d(zlib_datas_to_decode): #decompress zlib
  return zlib.decompress(zlib_datas_to_decode)
datas_d = zlib_d(datas)

def base64_d(base64_datas_to_decode): #decompress base64
  return base64.b64decode(base64_datas_to_decode)
datas_d_clear = base64_d(datas_d)
send_datas(datas_d_clear)

print('Deconnexion.')
client.close()
