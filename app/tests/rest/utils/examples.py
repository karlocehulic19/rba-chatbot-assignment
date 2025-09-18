import collections
from utils.synonims import synonims

# class for subsets of examples...tuple
# etc. default, modified, intermingled...


class Examples:
    SYNONIM_SUBTYPE = "synonims"

    def __init__(self):
        self.examples = collections.defaultdict(list)

    def add_example(self, subtype, examples):
        self.examples[subtype] = examples
        self.add_example_synonims(examples)

    def get_subexample(self, subtype):
        return self.examples[subtype]

    def get_all_examples(self):
        all_examples = []
        for subset_example in self.examples.values():
            for example in subset_example:
                all_examples.append(example)

        return all_examples

    def add_example_synonims(self, examples):
        for example in examples:
            words = example.split(" ")
            for i in range(len(words)):
                word = words[i].lower()
                if word not in synonims:
                    continue
                for synonim in synonims[word]:
                    self.examples[Examples.SYNONIM_SUBTYPE].append(" ".join(
                        words[:i] + [synonim] + words[i + 1:]))

    def get_all_synonims(self):
        return self.examples[Examples.SYNONIM_SUBTYPE]
