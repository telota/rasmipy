import os

import hug

from rasmipy import rasmify


listen_port = int(os.getenv('PORT', 8000))
get_text_type = hug.types.shorter_than(int(os.getenv('MAX_GET_PARAMETER_LENGTH', 1024)))


@hug.get('/')
def rasmify_get(text: get_text_type):
    return rasmify(text)


@hug.post('/')
def rasmify_post(body: hug.types.text):
    return rasmify(body)


def serve():
    hug.API(__name__).http.serve(listen_port, display_intro=False)
