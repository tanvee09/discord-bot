import requests
import json
import webbrowser


def dog() :
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    return image_url