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
print('Flag :' + datas)
print('Deconnexion.')

client.close()


#########################################
OR
#########################################

import socket; import base64; import zlib

HOST = 'challenge01.root-me.org' # 212.129.38.224
PORT = 52022

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print('Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.')

def MsgSend(datas):
    try:
        client.send(datas)
        return client.recv(1024)
    except:
        ValueError# print('Envoi de :' + datas)
    # n = client.send(datas)
    # if (n != len(datas)):
    #     return 'Erreur envoi.'
    # else:
    #     return 'Envoi ok.', client.recv(1024)


def zlib_decode(datas):
    return zlib.decompress(datas)

def b64_decode(datas):
    return base64.b64decode(datas)

def close():
    client.close()

while True :
    user_input = input('Datas to send for connexion :')    
    datas_receives = MsgSend(user_input) # Send message of user
    print('Reception... \n' + datas_receives[1])
    datas_b64_decode = b64_decode(datas_receives[1])
  # Not finish yet




