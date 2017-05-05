import os
from signal import signal, SIGINT, SIGTERM

import hug

from rasmipy import rasmify


# configuration


listen_port = int(os.getenv('PORT', 8000))
get_text_type = hug.types.shorter_than(int(os.getenv('MAX_GET_PARAMETER_LENGTH', 1024)))


# signal handling


def sigint_handler(signum, frame):
    print('Keyboard interrupt.')
    raise SystemExit(0)


def sigterm_handler(signum, frame):
    print('Received SIGTERM.')
    raise SystemExit(0)


signal(SIGINT, sigint_handler)
signal(SIGTERM, sigterm_handler)


# endpoints


@hug.get('/')
def rasmify_get(text: get_text_type):
    return rasmify(text)


@hug.post('/')
def rasmify_post(body: hug.types.text):
    return rasmify(body)


# service app


def serve():
    hug.API(__name__).http.serve(listen_port, display_intro=False)
