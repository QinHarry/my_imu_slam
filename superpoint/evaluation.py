import argparse
from utils import VideoStreamer, SuperPointFrontend
import utils
import cv2
import os
import time
import numpy as np
import matplotlib.pyplot as plt

# Stub to warn about opencv version.
if int(cv2.__version__[0]) < 3: # pragma: no cover
    print('Warning: OpenCV 3 is not installed')

def corner_display(imgs, fe):
    img_final = []
    im1 = []
    y = []
    for img in imgs:
        start1 = time.time()
        pts, desc, heatmap = fe.run(img)
        end1 = time.time()
        points = utils.select_top_k(pts)
        im1.append(utils.draw_keypoints(img, points, (255, 1, 1)))
    # utils.plot_imgs(im1, ylabel='current solution', dpi=200, cmap='gray', titles=titles)
    img_final.append(im1)
    y.append('deep learning')
    im2 = []
    for img in imgs:
        dst = cv2.cornerHarris(img, 2, 3, 0.04)
        dst = cv2.dilate(dst, None)
        dst = np.array(dst)
        xs, ys = np.where(dst >= 0.00001)
        pts = np.zeros((3, len(xs)))
        pts[0, :] = ys
        pts[1, :] = xs
        pts[2, :] = dst[xs, ys]
        pts, _ = fe.nms_fast(pts, img.shape[0], img.shape[1], dist_thresh=fe.nms_dist)
        points = utils.select_top_k(pts)
        im2.append(utils.draw_keypoints(img, points, (255, 1, 1)))
    #utils.plot_imgs(im2, ylabel='harris', dpi=200, cmap='gray', titles=titles)
    img_final.append(im2)
    y.append('harris')

    im3 = []
    for img in imgs:
        #dst = cv2.cornerSubPix(img, dst, 500, 0.01, 10, )
        dst = cv2.goodFeaturesToTrack(img, 300, 0.01, 10, blockSize=3, k=0.04)
        dst = dst.astype(int)
        points = list(np.squeeze(dst).T)
        im3.append(utils.draw_keypoints(img, points, (255, 1, 1)))
    # utils.plot_imgs(im3, ylabel='Shi', dpi=200, cmap='gray', titles=titles)

    img_final.append(im3)
    y.append('subpix')

    im4 = []
    for img in imgs:
        fast = cv2.FastFeatureDetector_create(threshold=70, nonmaxSuppression=True)
        img = img * 255.
        img = np.uint8(img)
        kp = fast.detect(img, None)
        # kp.sort()
        # kp = kp[:300]
        pts = np.zeros((2, len(kp)), np.int)
        i = 0
        for k in kp:
            pts[0, i] = k.pt[0]
            pts[1, i] = k.pt[1]
            i += 1
        points = pts.tolist()
        im4.append(utils.draw_keypoints(img, points, (1, 255, 1)))
        # orb = cv2.ORB_create()
        # kp, des = orb.detectAndCompute(img, None)
        # print(type(kp[0]))
    img_final.append(im4)
    y.append('fast')
    title = '300 points'
    utils.plot_imgs(img_final, ylabel=y, dpi=200, cmap='gray', title=title)

def match(imgs1, imgs2, fe):
    size = len(imgs1)
    _, ax = plt.subplots(size, 4, figsize=(12*4, 20))
    ax[0][0].set_title('ORB')
    ax[0][1].set_title('SIFT')
    ax[0][2].set_title('LIFT')
    ax[0][3].set_title('Deeper')
    for i in range(size):
        img1 = imgs1[i]
        img2 = imgs2[i]
        # pts1, desc1, heatmap1 = fe.run(img1)
        # pts2, desc2, heatmap2 = fe.run(img2)
        img1 = img1 * 255.
        img1 = np.uint8(img1)
        img2 = img2 * 255.
        img2 = np.uint8(img2)


        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:200], None, flags=2)
        if img3.shape[-1] == 3:
            img3 = img3[..., ::-1]  # BGR to RGB
        ax[i][0].imshow(img3)

        sift = cv2.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.4 * n.distance:
                good.append([m])
        img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
        ax[i][1].imshow(img3)

        for m, n in matches:
            if m.distance < 0.42 * n.distance:
                good.append([m])
        img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
        ax[i][2].imshow(img3)

        for m, n in matches:
            if m.distance < 0.45 * n.distance:
                good.append([m])
        img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
        ax[i][3].imshow(img3)


        # Too bad of superpoints
        # pts1 = pts1.astype(int)
        # idx1 = np.argsort(-pts1)[::-1][0][:100]
        # points1 = []
        # for i in idx1:
        #     points1.append(cv2.KeyPoint(x=pts1[0][i], y=pts1[1][i], _size=1))
        # desc1 = desc1.T[idx1]
        # pts2 = pts2.astype(int)
        # idx2 = np.argsort(-pts2)[::-1][0][:100]
        # points2 = []
        # for i in idx2:
        #     points2.append(cv2.KeyPoint(x=pts2[0][i], y=pts2[1][i], _size=1))
        # desc2 = desc2.T[idx1]
        # matches = bf.knnMatch(desc1, desc2, k=2)
        # good = []
        # for m, n in matches:
        #     if m.distance < 0.75 * n.distance:
        #         good.append([m])
        # img4 = cv2.drawMatchesKnn(img1, points1, img2, points2, good, None, flags=2)
        # ax[3].imshow(img4)

    plt.tight_layout()
    # plt.savefig('matcher.png')
    plt.show()

if __name__ == '__main__':

    print('start')
    parser = argparse.ArgumentParser(description='Detector repeatability')
    # parser = argparse.ArgumentParser(description='PyTorch SuperPoint Demo.')
    parser.add_argument('input', type=str, default='', help='Image directory ')
    parser.add_argument('--H', type=int, default=600,
                        help='Input image height (default: 600).')
    parser.add_argument('--W', type=int, default=800,
                        help='Input image width (default:800).')
    parser.add_argument('--img_glob', type=str, default='*.png',
                        help='Glob match if directory of images is specified (default: \'*.png\').')
    parser.add_argument('--weights_path', type=str, default='superpoint_v1.pth',
                        help='Path to pretrained weights file (default: superpoint_v1.pth).')
    parser.add_argument('--nms_dist', type=int, default=4,
                        help='Non Maximum Suppression (NMS) distance (default: 4).')
    parser.add_argument('--conf_thresh', type=float, default=0.015,
                        help='Detector confidence threshold (default: 0.015).')
    parser.add_argument('--nn_thresh', type=float, default=0.7,
                        help='Descriptor matching threshold (default: 0.7).')
    parser.add_argument('--skip', type=int, default=1,
                        help='Images to skip if input is movie or directory (default: 1).')
    opt = parser.parse_args()
    print(opt)
    vs = VideoStreamer(opt.input, 0, opt.H, opt.W, opt.skip, opt.img_glob)

    print('==> Loading pre-trained network.')
    # This class runs the SuperPoint network and processes its outputs.
    fe = SuperPointFrontend(weights_path=opt.weights_path,
                            nms_dist=opt.nms_dist,
                            conf_thresh=opt.conf_thresh,
                            nn_thresh=opt.nn_thresh)
    print('==> Successfully loaded pre-trained network.')

    # corner detector
    # img0 = vs.read_image(vs.listing[0], vs.sizer)
    # img1 = vs.read_image(vs.listing[1], vs.sizer)
    # corner_display([img0, img1], fe)

    # matcher
    l = len(vs.listing)
    x = []
    y = []
    for i in range(l):
        if i % 2 == 0:
            x.append(vs.read_image(vs.listing[i], vs.sizer))
        else:
            y.append(vs.read_image(vs.listing[i], vs.sizer))
    match(x, y, fe)