import cv2
import numpy as np

# Read image
img = cv2.imread('image.jpg', 0)

# High-boost factor
A = 1.5

# Blur the image
blur = cv2.GaussianBlur(img,(5,5),0)

# High-boost sharpening
highboost = cv2.addWeighted(img, A, blur, -1, 0)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("High Boost Image", highboost)

cv2.waitKey(0)
cv2.destroyAllWindows()