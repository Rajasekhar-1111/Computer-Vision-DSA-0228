import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

rows, cols = img.shape[:2]

# Source points
pts_src = np.float32([[50,50], [200,50], [50,200], [200,200]])

# Destination points
pts_dst = np.float32([[10,100], [220,50], [100,250], [250,220]])

# Compute Homography matrix
H, status = cv2.findHomography(pts_src, pts_dst)

# Apply transformation
result = cv2.warpPerspective(img, H, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
