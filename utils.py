import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
VERIFY_TOKEN = "EAACxcf8Gk5ABAMNS7th1fmr8OkKE6mLlindxEnx6Wt9Eyk0jmpzbNU8Jua51DHIJFZA6qnzokXwFTSaP2dBCErc1vZB3HmTTKsuZAW136zT8zMXVxv8OMuCgUwM8owHZANdeEDykoNbz9Cnu8V6XQdIGSS8zRBwGjv5rTe0ZC3R8VkEr2e1LK"

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
