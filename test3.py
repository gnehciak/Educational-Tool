import time, os
length = 32
with open('data/fireworks.txt') as f:
    frames = []
    f = f.readlines()
    single = []
    for i, line in enumerate(range(0, len(f), length)):
        single = []
        i *= length
        for a in range(length):
            single.append(f[i+a])
        frames.append(''.join(single))
while True:
    for frame in frames:
        print(frame)
        time.sleep(0.02)
        #os.system('CLS')