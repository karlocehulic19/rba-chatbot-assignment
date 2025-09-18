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
            self.intents = []

        return Setup.singleton

    def get_all_intents(self):
        is_already_computed = len(self.intents) != 0
        if is_already_computed:
            return self.intents

        json = requests \
            .get(Setup.API_URL + "/static/intents.json").json()
        self.intents = []

        for obj in json:
            self.intents.append(Intent(obj["intent"], obj["canonical_reply"],
                                       obj["examples"]))

        return self.intents
