import requests

API_URL = "http://localhost:8000/"

intents = []


class Intent:
    def __init__(self, intent, canonical_reply, examples):
        self.type = type
        self.canonical_reply = canonical_reply
        self.examples = examples


def get_all_intents():
    global intents
    is_already_computed = len(intents) != 0
    if is_already_computed:
        return intents

    json = requests \
        .get(API_URL + "/static/intents.json").json()
    intents = []

    for obj in json:
        intents.append(Intent(obj["intent"], obj["canonical_reply"],
                              obj["examples"]))

    return intents
