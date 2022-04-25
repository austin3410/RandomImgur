import random
import requests
import shutil
import base64
import os

possible_chars = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz"
possible_ext = [".jpg"]
image_dir = "images//"

with open("404.jpg", "rb") as notfound_file:
    notfound = base64.b64encode(notfound_file.read())

while True:
    chars = ""

    for i in range(0,5):
        chars += random.choice(possible_chars)

    # Troubleshoot
    #chars = "4eMJ1"
    for ext in possible_ext:
        r = requests.get(f"https://i.imgur.com/{chars}{ext}", stream=True)

        if r.status_code == 200:
            #r.raw.decode_content = True
            with open(f"{image_dir}{chars}{ext}", "wb") as file:
                shutil.copyfileobj(r.raw, file)

        with open(f"{image_dir}{chars}{ext}", "rb") as file:
            file = base64.b64encode(file.read())

        if file == notfound:
            os.remove(f"{image_dir}{chars}{ext}")
        else:
            print(f"Grabbed: {chars}{ext}")



