import requests
import os

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
#ACCESS_TOKEN = "EAACxcf8Gk5ABAEZBYaMaI9HgZCuica2aSxp4PL64ROFEKlSJ7GVbjA1iUr6MVDso84Rpi9yHxZABaYzRoDplVNtZBFv5vurZAMVg01ubQPyLDhgZBbx13yCxNZCTBVZAPvZCI98ZA6NCIOpZB9wpLS57MbNT7g5yYuZBKFQ77b0e1C7pPLdSBkv1ldeN"

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_image_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"attachment": {"type": "image","payload": {"url": text}}}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
