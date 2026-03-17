import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('image.jpg', 0)

# Create structuring element (kernel)
kernel = np.ones((5,5), np.uint8)

# Apply Top Hat transformation
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Top Hat Image", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()