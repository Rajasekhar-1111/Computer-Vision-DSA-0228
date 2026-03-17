import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread('image.jpg', 0)

# Sobel gradient masks
Gx = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])

Gy = np.array([[-1,-2,-1],
               [0,0,0],
               [1,2,1]])

# Apply gradient filters
grad_x = cv2.filter2D(img, -1, Gx)
grad_y = cv2.filter2D(img, -1, Gy)

# Combine gradients
gradient = cv2.add(grad_x, grad_y)

# Sharpen image
sharpened = cv2.add(img, gradient)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()