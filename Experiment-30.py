import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('image.jpg', 0)

# Create structuring element (kernel)
kernel = np.ones((5,5), np.uint8)

# Apply Black Hat transformation
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Black Hat Image", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()