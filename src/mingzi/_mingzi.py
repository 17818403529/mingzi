from random import random, choice
import json
import os


"""
the probability distribution data, and the
alternative dataset collated from network
"""

try:
    with open(os.path.split(os.path.realpath(__file__))[0] + "\\data.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
except FileNotFoundError:
    with open(os.path.split(os.path.realpath(__file__))[0] + "/data.json", "r", encoding="UTF-8") as f:
        data = json.load(f)

samples = []
for i in data["surname"].keys():
    samples += [i] * (int(data["surname"][i] * 30000))


def gen_surname(com_rate=0.001):
    if random() < com_rate:
        return choice(data["com_surname"])
    else:
        return choice(samples)


def mingzi(volume=1, female_rate=0.5, single_rate=0.5, com_rate=0.001, show_gender=False, alt_surname=[]):
    output = []
    for i in range(volume):
        if alt_surname == []:
            surname = gen_surname(com_rate=com_rate)
        else:
            surname = choice(alt_surname)

        length = random() < single_rate
        gender = random() >= female_rate

        if gender:
            if length:
                name = surname + choice(data["male_single"])
            else:
                name = surname + choice(data["male_double"])
        else:
            if length:
                name = surname + choice(data["female_single"])
            else:
                name = surname + choice(data["female_double"])

        if show_gender:
            output.append([name, ["女", "男"][gender]])
        else:
            output.append(name)
    return output
