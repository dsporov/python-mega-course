import cv2
img = cv2.imread("galaxy.jpg", 0) # -1, 0, 1 for ARGB, greyscale, RGB
print img
print img.shape
print img.ndim

img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imwrite("galaxy_shrinked.jpg", img)

cv2.imshow("Galaxy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

