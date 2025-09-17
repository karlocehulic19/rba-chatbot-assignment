# class for subsets of examples...tuple
# etc. default, modified, intermingled...
class Examples:
    def __init__(self):
        self.examples = {}

    def add_example(self, subtype, examples):
        self.examples[subtype] = examples

    def get_subexample(self, subtype):
        return self.examples[subtype]

    def get_all_examples(self):
        all_examples = []
        for subset_example in self.examples.values():
            for example in subset_example:
                all_examples.append(example)

        return all_examples
