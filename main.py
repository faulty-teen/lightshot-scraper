from termcolor import colored
import threading
import requests
import random
import string
import base64
import json
import os
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image
import config

WEBHOOK_URL = config.WEBHOOK_URL
valid = 0
invalid = 0
proxy_num = 0
proxies = []
save = config.SAVE_IMAGES
THREADS = config.THREADS

with open('data.json') as fp:
    Base64FakeImages = json.load(fp)

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

def grab_proxies():
    global proxies
    proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=5000&country=all&ssl=all&anonymity=all').text.splitlines()
    print(f"[{colored('proxies reloaded', 'green', attrs=['bold'])}]")

def process_image(content):
    """
    Tries to load the image to determine if it is valid.
    If it loads normally, returns the original content with state "normal".
    If it fails, attempts to re-open and re-save it as PNG (fixing it) and returns that content with state "fixed".
    If both fail, returns (None, "failed").
    """
    try:
        image = Image.open(BytesIO(content))
        image.load()
        return content, "normal"
    except Exception as e:
        try:
            image = Image.open(BytesIO(content))
            new_buffer = BytesIO()
            image.convert('RGB').save(new_buffer, format="PNG")
            fixed_content = new_buffer.getvalue()
            fixed_image = Image.open(BytesIO(fixed_content))
            fixed_image.load()
            return fixed_content, "fixed"
        except Exception as ex:
            return None, "failed"

def checkifimageisvalid(arg):
    global valid, invalid, save
    response = requests.get(arg, headers=headers)
    if response.ok:
        uri = base64.b64encode(response.content).decode("utf-8")
        if uri in Base64FakeImages.values():
            invalid += 1
            return
        
        image_data, state = process_image(response.content)
        if image_data is None:
            invalid += 1
            print("[" + colored('invalid image', 'red', attrs=['bold']) + "] " + arg + f"    [{valid} / {invalid}]")
            return

        valid += 1

        parsed = urlparse(arg)
        base_name = os.path.basename(parsed.path)
        if not base_name or '.' not in base_name:
            if state == "fixed":
                ext = "png"
            else:
                content_type = response.headers.get('Content-Type', '')
                if '/' in content_type:
                    ext = content_type.split('/')[-1]
                else:
                    ext = 'jpg'
            base_name = f'image_{valid}.{ext}'
        else:
            if state == "fixed":
                base_name = os.path.splitext(base_name)[0] + ".png"

        mime = response.headers.get('Content-Type') if state == "normal" else "image/png"
        files = {"file": (base_name, image_data, mime)}
        r = requests.post(WEBHOOK_URL, files=files)
        if r.ok:
            print("[" + colored(f'sent image to discord', 'green', attrs=['bold']) + "] " + arg)
        else:
            print("[" + colored('failed to send to discord', 'yellow', attrs=['bold']) + "] " + arg)

        if save:
            if not os.path.exists('./images'):
                os.makedirs('./images')
            file_path = os.path.join("./images", base_name)
            with open(file_path, 'wb') as f:
                f.write(image_data)

def main(proxy):
    global valid, invalid
    code = "1" + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
    try:
        check = requests.get(f'https://prnt.sc/{code}', headers=headers, proxies={'https': 'http://%s' % proxy}).text
        if 'name="twitter:image:src" content="' in check and '0_173a7b_211be8ff' not in check and 'ml3U3Pt' not in check:
            url = check.split('name="twitter:image:src" content="')[1].split('"/> <meta')[0]
            checkifimageisvalid(url)
        else:
            invalid += 1
            print("[" + colored('attempts', 'red', attrs=['bold']) + "] " + str(valid + invalid), end="\r")
    except Exception as e:
        pass

test_data = {
    'content': 'WEBHOOK CONNECTED'
}
test = requests.post(WEBHOOK_URL, json=test_data)
if not test.ok:
    print(f"[{colored('Webhook URL Invalid. Exiting script...', 'red', attrs=['bold'])}]")
    exit()

grab_proxies()

while True:

    if threading.active_count() <= THREADS:
        try:
            threading.Thread(target=main, args=(proxies[proxy_num],)).start()
            proxy_num += 1
            if proxy_num >= len(proxies):
                proxy_num = 0
                proxies.clear()
                grab_proxies()
        except Exception as e:
            pass
