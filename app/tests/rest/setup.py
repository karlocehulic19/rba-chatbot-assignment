import requests


class Intent:
    def __init__(self, intent, canonical_reply, examples):
        self.type = type
        self.canonical_reply = canonical_reply
        self.examples = examples


class Setup:
    singleton = None
    API_URL = "http://localhost:8000/"

    def __init__(self):
        if not Setup.singleton:
            Setup.singleton = self

        return Setup.singleton

    def get_all_prompts():
        json = requests \
            .get(Setup.API_URL + "/static/intents.json").json()
        intents = []

        for obj in json:
            intents.append(Intent(obj["intent"], obj["canonical_reply"],
                                  obj["examples"]))
