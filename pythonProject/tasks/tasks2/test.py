import random
import string
from random import randint


def generate_random_string():
    length = randint(5, 15)
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    s = ["".join(dict.fromkeys(rand_string))]
    return s[0]


def file_names():
    s = []
    for i in range(10):
        s.append(generate_random_string())
    for i in range(len(s)):
        if len(s[i]) < len(max(s, key=len)):
            temp = len(max(s, key=len)) - len(s[i])
            for y in range(temp):
                s[i] += "_"
    for i in range(len(s)):
        print(s[i])
