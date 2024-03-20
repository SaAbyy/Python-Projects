import requests
import pytesseract
import base64
from PIL import Image
from bs4 import BeautifulSoup
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\****\****\****\tesseract.exe'

url = 'http://challenge01.root-me.org/programmation/ch8/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = str(soup.find('img'))

# Utilisation de regex pour extraire la partie en base64
base64_data = re.search(r'base64,(.*)"', results).group(1)

# Décodage de la chaîne base64
decoded_data = base64.b64decode(base64_data)

# Nom du fichier dans lequel vous souhaitez enregistrer l'image
file_name = "captcha.png"

# Enregistrement de l'image dans un fichier
with open(file_name, "wb") as file:
    file.write(decoded_data)

print(f"L'image a été enregistrée sous {file_name}")

def solve_captcha(image_path):
    captcha_image = Image.open(image_path)
    captcha_text = pytesseract.image_to_string(captcha_image)
    return captcha_text

captcha_solution = solve_captcha('captcha.png')
print("CAPTCHA Solution:",captcha_solution)

data = {
    'cametu': captcha_solution
}

print(data)

# Poster les données
response = requests.post(url, data=data)

soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find('p')

# Afficher la réponse
print(results)
