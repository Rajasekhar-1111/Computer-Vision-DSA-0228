import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('image.jpg', 0)

# Create structuring element (kernel)
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()