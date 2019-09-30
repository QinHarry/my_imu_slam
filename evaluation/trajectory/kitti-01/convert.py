
orb = []
gt = []
vins = []

with open('vins.kitti', 'r') as f:
    vins = f.readlines()

with open('01.txt', 'r') as f:
    gt = f.readlines()

with open('kitti-orb-origin.kitti', 'r') as f:
    orb = f.readlines()

m = min(len(vins), len(gt), len(orb))

rate1 = 1.0 * len(vins) / m
rate2 = 1.0 * len(gt) / m
rate3 = 1.0 * len(orb) / m


orbStr = ''
gtStr = ''
vinsStr = ''

for i in range(m):
    index = round(i * rate1)
    if index < len(vins):
        vinsStr = vinsStr + vins[index]
    index = round(i * rate2)
    if index < len(gt):
        gtStr = gtStr + gt[index]
    index = round(i * rate3)
    if index < len(orb):
        orbStr = orbStr + orb[index]

with open('vins-new.kitti', 'w') as f:
    f.write(vinsStr)
with open('gt.kitti', 'w') as f:
    f.write(gtStr)
with open('orb.kitti', 'w') as f:
    f.write(orbStr)
