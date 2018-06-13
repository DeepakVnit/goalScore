from channels import Group
from .views import get_goals

def ws_message(message):
    print(message.content['text'])
    data = get_goals()
    Group('users').send({'text': data})

def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({'text': 'connected'})


def ws_disconnect(message):
    Group('users').send({'text': 'disconnected'})
    Group('users').discard(message.reply_channel)
