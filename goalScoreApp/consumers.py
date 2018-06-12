from channels import Group
import threading
import random


def sendmsg(num):
    Group('users').send({'text': num})


t = 0


def periodic():
    global t;
    n = random.randint(10, 200);
    sendmsg(str(n))
    t = threading.Timer(5, periodic)
    t.start()


def ws_message(message):
    global t
    print(message.content['text'])
    if (message.content['text'] == 'start'):
        periodic()
    else:
        t.cancel()


def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({'text': 'connected'})


def ws_disconnect(message):
    Group('users').send({'text': 'disconnected'})
    Group('users').discard(message.reply_channel)