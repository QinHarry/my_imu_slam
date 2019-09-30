
kitti = []
gt = []

with open('vins.kitti', 'r') as f:
    kitti = f.readlines()

with open('00.txt', 'r') as f:
    gt = f.readlines()

rate = 1.0 * len(kitti) / len(gt)

kittiStr = ''

for i in range(len(gt)):
    index = round(i * rate)
    if index < len(kitti):
        kittiStr = kittiStr + kitti[index]

with open('new-vins.kitti', 'w') as f:
    f.write(kittiStr)