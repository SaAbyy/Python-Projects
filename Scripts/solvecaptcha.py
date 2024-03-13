import requests
import pytesseract
import base64
from PIL import Image
from bs4 import BeautifulSoup


url = 'http://challenge01.root-me.org/programmation/ch8/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('img')

image = base64.b64decode(results)
f = open("captcha.png", "w")
f.write(image)
f.close()

def solve_captcha(image_path):
    captcha_image = Image.open(image_path)
    captcha_text = pytesseract.image_to_string(captcha_image)
    return captcha_text

captcha_solution = solve_captcha('captcha.png')
print("CAPTCHA Solution:", captcha_solution)

data = {
    'cametu' : captcha_solution
}

print(requests.post(url, data=data))





