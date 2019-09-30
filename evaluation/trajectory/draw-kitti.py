import matplotlib.image as mpimg
import matplotlib.pyplot as plt



orb = mpimg.imread('kitti-00/t_orb.png')
dp_vi = mpimg.imread('kitti-00/t_dp_vi.png')

_, ax = plt.subplots(1, 2)

ax[0].imshow(orb)
ax[0].set_title('ORB')

ax[1].imshow(dp_vi)
ax[1].set_title('DP-VI')

plt.tight_layout()
plt.show()