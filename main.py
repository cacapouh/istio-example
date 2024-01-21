import os

from bottle import route, run


count = 0


@route('/')
def index():
    global count
    count = count + 1
    return "{}: {}!".format(count, os.environ["HOSTNAME"])


run(host='0.0.0.0', port=8080)
