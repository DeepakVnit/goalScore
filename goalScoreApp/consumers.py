from channels import Group

def ws_message(message):
    print(message.content['text'])
    Group('users').send({'text': "message"})

def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({'text': 'connected'})


def ws_disconnect(message):
    Group('users').send({'text': 'disconnected'})
    Group('users').discard(message.reply_channel)
