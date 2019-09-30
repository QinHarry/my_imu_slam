import matplotlib.image as mpimg
import matplotlib.pyplot as plt



orb = mpimg.imread('euroc-orb-t.png')
orb_vi = mpimg.imread('euroc-orb-vi-t.png')
dp = mpimg.imread('euroc-dp-t.png')
dp_vi = mpimg.imread('euroc-dp-vi-t.png')

_, ax = plt.subplots(2, 2)

ax[0][0].imshow(orb)
ax[0][0].set_title('ORB')

ax[0][1].imshow(orb_vi)
ax[0][1].set_title('ORB-VI')

ax[1][0].imshow(dp)
ax[1][0].set_title('DP')

ax[1][1].imshow(dp_vi)
ax[1][1].set_title('DP-VI')

plt.tight_layout()
plt.show()