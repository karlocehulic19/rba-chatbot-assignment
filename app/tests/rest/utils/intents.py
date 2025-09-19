from .examples import Examples


class Intent:
    def __init__(self, type, canonical_reply, examples):
        self.type = type
        self.canonical_reply = canonical_reply
        self.examples = Examples()
        self.examples.add_example(Examples.DEFAULT_SUBTYPE, examples)
