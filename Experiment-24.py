import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('image.jpg', 0)

# Create kernel (structuring element)
kernel = np.ones((5,5), np.uint8)

# Apply erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()