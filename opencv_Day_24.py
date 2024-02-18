import cv2
import numpy as np

img1 = cv2.imread('tarun.jpeg')
img2 = cv2.imread('nitin.jpeg')

tarun = cv2.resize(img1, (400, 400))
nitin = cv2.resize(img2, (400, 400))

tarun_nitin = np.hstack((tarun[:, :200], nitin[:, 200:]))
cv2.imshow('merge', tarun_nitin)

gp_tarun = [tarun]
gp_nitin = [nitin]

# Generating Gaussian Pyramid for Tarun
for i in range(6):
    tarun = cv2.pyrDown(tarun)
    gp_tarun.append(tarun)

# Generating Gaussian Pyramid for Nitin
for i in range(6):
    nitin = cv2.pyrDown(nitin)
    gp_nitin.append(nitin)

# Generating Laplacian Pyramid for Tarun
lp_tarun = [gp_tarun[5]]
for i in range(5, 0, -1):
    gaussian_extended_tarun = cv2.pyrUp(gp_tarun[i])
    h, w, _ = gp_tarun[i - 1].shape
    gaussian_extended_tarun = cv2.resize(gaussian_extended_tarun, (w, h))
    laplacian_tarun = cv2.subtract(gp_tarun[i - 1], gaussian_extended_tarun)
    lp_tarun.append(laplacian_tarun)
    cv2.imshow(str(i), laplacian_tarun)

# Generating Laplacian Pyramid for Nitin
lp_nitin = [gp_nitin[5]]
for i in range(5, 0, -1):
    gaussian_extended_nitin = cv2.pyrUp(gp_nitin[i])
    h, w, _ = gp_nitin[i - 1].shape
    gaussian_extended_nitin = cv2.resize(gaussian_extended_nitin, (w, h))
    laplacian_nitin = cv2.subtract(gp_nitin[i - 1], gaussian_extended_nitin)
    lp_nitin.append(laplacian_nitin)
    cv2.imshow(str(i), laplacian_nitin)

# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lp_tarun, lp_nitin):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, :int(cols/2)], lb[:, int(cols/2):]))
    LS.append(ls)

# Now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    h, w, _ = LS[i].shape
    ls_ = cv2.resize(ls_, (w, h))
    ls_ = cv2.add(ls_, LS[i])

cv2.imshow('tarun_nitin', ls_)
cv2.waitKey(0)
cv2.destroyAllWindows()
