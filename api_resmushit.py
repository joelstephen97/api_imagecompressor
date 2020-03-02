import requests
import urllib.request
import os
import json

cwd = os.getcwd()


def api_image_compressor(dest,filename):
    url = "http://api.resmush.it/ws.php?img=%s"%(dest)

    response = requests.request("POST",url=url)
    response_json = response.json()

    try:
        urllib.request.urlretrieve(response_json['dest'], filename)
        print("Image has been downloaded successfully")
    except KeyError:
        print("Error, recheck your link. ")

def get_values():
    source = input('Enter URL of Image to optimize : ')
    filename = input("Enter destination filename you want give : ")
    filename = filename+".jpg"

    api_image_compressor(dest=source, filename=filename)


get_values()
