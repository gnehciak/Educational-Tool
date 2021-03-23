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
for frame in frames:
    print(frame)
    time.sleep(0.05)
    os.system('CLS')




def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(prime_factors(int(input('num'))))