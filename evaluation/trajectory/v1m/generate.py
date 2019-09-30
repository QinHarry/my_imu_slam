import random

sp = ''

def value(input, r):
    flag = random.randint(-1, 1)
    output = float(input) * (1 + r * flag)
    output = round(output, 6)
    return str(output)

def valueQ(input, r):
    output = float(input) * r
    output = round(output, 6)
    return str(output)

with open('data.tum', 'r') as f:
    r = random.uniform(0.2, 0.3)
    cnt = 0
    for line in f.readlines():
        cnt = cnt + 1
        if cnt % 10 == 0:
            arr = line.split(' ')
            sp = sp + arr[0] + ' '
            for i in range(1, 4):
                sp = sp + value(arr[i], r) + ' '
            for i in range(4, 8):
                sp = sp + valueQ(arr[i], 1 + 0.0001) + ' '
            sp = sp[:-1]
            sp = sp + '\n'

sp = sp[:-1]


with open('sp.txt', 'w') as f:
    f.write(sp)



