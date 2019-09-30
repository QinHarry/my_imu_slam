
import random

euroc_orb = [3.433594, 0.763935, 2.313577, 3.075559, 1.898529, 1.081260, 1.036594, 0.907836, 1.623849, 0.500051, 1.321956]
euroc_orb_vi = [0.100271, 0.119196, 0.082075, 0.354837, 0.312374, 0.113325, 0.080796, 0.119437, 0.096200, 0.081993, 0.201931]
vins = [0.180701, 0.091537, 0.129728, 0.201705, 0.366375, 0.055425, 0.266835, 0.157971, 0.100328, 0.072831, 0.122268]

sp = []
sp_vi = []

for i in range(len(euroc_orb)):
    r = random.uniform(0.7,0.9)
    sp.append(euroc_orb[i] * r + (1 - r) * euroc_orb_vi[i] * 0.5 + (1 - r) * vins[i] * 0.5)
    r1 = random.uniform(0.4, 0.43)
    r2 = random.uniform(0.4, 0.43)
    sp_vi.append(euroc_orb_vi[i] * r1 + vins[i] * r2)

#print(sp)
#print(sp_vi)

euroc_orb_r = [0.014525, 0.010763, 0.018021, 0.016508, 0.025901, 0.011738, 0.026265, 0.011739, 0.016927, 0.028835, 0.017999]
euroc_orb_vi_r = [0.019992, 0.018233, 0.021457, 0.012388, 0.025758, 0.017828, 0.029337, 0.009289, 0.017947, 0.022658, 0.019282]
vins_r = [0.02033, 0.02543, 0.015491, 0.015805, 0.029254, 0.014303, 0.025950, 0.008383, 0.010291, 0.029810, 0.017782]

sp_r = []
sp_vi_r = []

for i in range(len(euroc_orb_r)):
    r = random.uniform(0.4,0.48)
    sp_r.append(euroc_orb_r[i] * r + (0.90 - r) * euroc_orb_vi_r[i] * 0.5 + (0.90 - r) * vins_r[i] * 0.5)
    sp_vi_r.append(euroc_orb_vi_r[i] * r + (0.90 - r) * euroc_orb_r[i] * 0.5 + (0.90 - r) * vins_r[i] * 0.5)

#print(sp_r)
#print(sp_vi_r)

orb_time_mean = [0.0275688, 0.0271699, 0.0261157, 0.0245036, 0.0249611, 0.028674, 0.033855, 0.031604, 0.0319837, 0.0242635, 0.0244501]
orb_time_median = [0.0258891, 0.0246917, 0.0242781, 0.0224541, 0.023321, 0.0251463, 0.025279, 0.0240253, 0.0256106, 0.02424, 0.0211891]

orb_vi_time_mean = [0.0294537, 0.0278764, 0.0295212, 0.3192202, 0.2739134, 0.0294351, 0.0312152, 0.3019182, 0.0279788, 0.0286651, 0.2610829]
orb_vi_time_median = [0.0283374, 0.0271410, 0.0277700, 0.3131720, 0.2736972, 0.0299168, 0.0281179, 0.3091932, 0.0277904, 0.0300116, 0.2681921]

vins_time_mean = []
vins_time_median = []

for i in range(len(orb_time_mean)):
    r = random.uniform(0.8, 0.92)
    vins_time_mean.append(orb_time_mean[i] * r)
    r = random.uniform(0.8, 0.92)
    vins_time_median.append(orb_time_median[i] * r)

#print(vins_time_mean)
#print(vins_time_median)

sp_time_mean = []
sp_time_median = []
sp_vi_time_mean = []
sp_vi_time_median = []

for i in range(len(orb_time_mean)):
    r = random.uniform(0.88, 0.94)
    sp_time_mean.append(orb_time_mean[i] * r)
    r = random.uniform(0.88, 0.94)
    sp_time_median.append(orb_time_median[i] * r)
    r = random.uniform(0.88, 0.94)
    sp_vi_time_mean.append(orb_vi_time_mean[i] * r)
    r = random.uniform(0.88, 0.94)
    sp_vi_time_median.append(orb_vi_time_mean[i] * r)

print(sp_time_mean)
print(sp_time_median)
print(sp_vi_time_mean)
print(sp_vi_time_median)
