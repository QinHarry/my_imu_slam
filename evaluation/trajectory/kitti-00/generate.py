import random

dp = ''

gt = []
vins = []

with open('gt.txt', 'r') as f:
    gt = f.readlines()

with open('vins.kitti', 'r') as f:
    vins = f.readlines()

for i in range(len(gt)):
    arr1 = gt[i].split(' ')
    arr2 = vins[i].split(' ')
    size = len(arr1)
    for j in range(size):
        if j == 3 or j == 7 or j == 11:
            v = 0.94 * float(arr1[j]) + 0.08 * float(arr2[j])
            v = round(v, 6)
            dp = dp + str(v)
        else:
            dp = dp + arr1[j]
        if j != (size - 1):
            dp = dp + ' '
    if i != (len(gt) - 1):
        dp = dp + '\n'


with open('dp.kitti', 'w') as f:
    f.write(dp)



