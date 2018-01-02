from markov import markov

with open("./data.txt") as f:
    data = f.read().split()

rule = markov.rule(data)

seed = ["今日", "は"]
print(markov.create_sentence(rule, seed=seed))
