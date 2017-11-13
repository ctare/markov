import random


class Data(dict):
    def __init__(self):
        self._source = []

    def add(self, *data):
        for d in data:
            self._source.append(d)

def rule(data, n=2):
    words = data._source
    n -= 1
    container = {}
    for i in range(len(words) - n - 2):
        target = container
        for w in words[i:i + n]:
            tmp = target.get(w, {})
            target[w] = tmp
            target = tmp
        tmp = target.get(words[i + n], [])
        tmp.append(words[i + n + 1])
        target[words[i + n]] = tmp
    return {"container": container, "n": n + 1}


def create_seed(rule):
    container = rule["container"]
    n = rule["n"]

    seed = []
    target = container
    for i in range(n):
        key = random.choice(list(target.keys()))
        seed.append(key)
        target = target[key]
    seed.append(random.choice(target))
    return seed


def predict(rule, seed):
    container = rule["container"]
    n = rule["n"]
    if len(seed) < n:
        raise ValueError("plz: seed len >= n")

    target = container
    try:
        for w in seed[-n : len(seed)]:
            target = target[w]
    except KeyError:
        return None
    return target


def create_sentence(rule, end_rule=lambda x: x[-1].endswith("。"), seed=None):
    if not seed:
        sentence = create_seed(rule)
    else:
        sentence = seed

    if not callable(end_rule):
        raise TypeError("end_rule must be callable")

    while not sentence[-1].endswith("。"):
        candidate = predict(rule, sentence)
        if candidate:
            sentence.append(random.choice(candidate))
        else:
            raise ValueError(sentence)
    return sentence
