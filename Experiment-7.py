import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

rows, cols, ch = img.shape

# Three points in the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Three points in the output image
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Affine transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
result = cv2.warpAffine(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
