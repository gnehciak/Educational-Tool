import time, os
from modules.miscellaneous import clear

def print_firework():
    length = 32
    with open('data/txt/fireworks.txt') as f:
        frames = []
        f = f.readlines()
        single = []
        for i, line in enumerate(range(0, len(f), length)):
            single = []
            i *= length
            for a in range(length):
                single.append(f[i+a])
            frames.append(''.join(single))
    for frame in frames:
        print(frame)
        time.sleep(0.01)
        clear()
