import requests


class Client:
    url_base = "https://brasil.io/api/dataset/covid19/{}"
    _request = requests

    def __init__(self):
        pass

    # TODO: set common interface to parse data
