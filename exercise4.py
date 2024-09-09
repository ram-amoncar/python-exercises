# Encoder & Decoder

from random import shuffle

alphabets = [*"abcdefghijklmnopqrstuvwxyz"]


def code(string: str):
    string = string.lower()
    l = len(string)
    if l < 3:
        return "".join([string[i] for i in range(l - 1, -1, -1)])
    else:
        shuffle(alphabets)
        return "".join(alphabets[-3:]) + string[1:] + string[0] + "".join(alphabets[:3])


def decode(string: str):
    string = string.lower()
    l = len(string)
    if l < 3:
        return "".join([string[i] for i in range(l - 1, -1, -1)])
    else:
        return string[-4:-3] + string[3:-4]


print("Two letters word")
c = code("at")
print("Coded:", c)
print("Decoded:", decode(c))

print()

print("More than 2 letters word")
c = code("hidden")
print("Coded:", c)
print("Decoded:", decode(c))
