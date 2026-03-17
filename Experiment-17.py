import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('image.jpg', 0)

# Laplacian mask with diagonal neighbors
kernel = np.array([[1,1,1],
                   [1,-8,1],
                   [1,1,1]])

# Apply Laplacian filter
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen image
sharpened = img - laplacian

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()