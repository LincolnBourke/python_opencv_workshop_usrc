import cv2
import numpy as np 

# open image and scale to reasonable size for viewing
img = cv2.imread("Photos\space_image.jpg")
img = cv2.resize(img, (int(img.shape[1]*0.5), int(img.shape[0]*0.5)))
cv2.imshow("Original image", img)

# rescale to half size
width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
new_dim = (width, height)

img_rescaled = cv2.resize(img, new_dim)
cv2.imshow("Image scaled to half size", img_rescaled)


# draw rectangle at centre of image
img_drawn = np.copy(img)
bottom_corner = (int(img_drawn.shape[1] * 0.5 - 200), int(img_drawn.shape[0] * 0.5 - 150))
top_corner = (int(img_drawn.shape[1] * 0.5 + 200), int(img_drawn.shape[0] * 0.5 + 150))

cv2.rectangle(img_drawn, bottom_corner, top_corner, (255, 255, 255), thickness=cv2.BORDER_DEFAULT)
cv2.imshow("Image with rectangle drawn at centre", img_drawn)


# pass through blur, greyscale and canny
img_processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_processed = cv2.GaussianBlur(img_processed, (9,9), cv2.BORDER_DEFAULT)
# probably not the best image choice for this....
img_processed = cv2.Canny(img_processed, 10, 20)
cv2.imshow("Image after passing through greyscale, blur and canny", img_processed)


# rotate by 45 degrees
rotMat = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 45, scale=1.0)

img_rotated = cv2.warpAffine(img, rotMat, (img.shape[1], img.shape[0]))
cv2.imshow("Image rotated 45 degrees", img_rotated)

cv2.waitKey(0)
