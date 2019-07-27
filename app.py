import requests
import random
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if (data['name'] != 'DEVEN BOT') & ('hi deven' in data['text'].lower()):
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    send_message(msg)

  return "ok", 200


def send_message(msg):
    message = 'yerrrrr deven'
    pic_url = "https://i.groupme.com/720x960.jpeg.631b921f22cd4507aa6cabcfb427d4ac"
    
    post_params = {
      "bot_id"  : os.getenv('BOT_ID'),
      "text"    : get_random_message(),
      "attachments" : [
        {
          "type"  : "image",
          "url"   : pic_url
        }
      ]
    }
    post_data = {'text':message, 'picture_url':get_random_pic_url()}
    
    requests.post('https://api.groupme.com/v3/bots/post', params = post_params, data=post_data)


def get_random_pic_url():

    with open('bot_urls.txt') as links:
        links_list = links.read().split('\n')
        links_len = len(links_list)
        random_index = int(random.random() * links_len)
        return links_list[random_index]


def get_random_message():

    if random.random() < .3:
        return ''
    else:
        with open('bot_messages.txt') as messages:
            txt = messages.read().split('\n')
            txt_len = len(txt)
            random_index = int(random.random() * txt_len)
            return txt[random_index]
