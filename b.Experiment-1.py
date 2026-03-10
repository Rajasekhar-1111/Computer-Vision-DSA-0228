import cv2

# Read image
img = cv2.imread("image2.jpg")

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (15,15), 0)

# Show result
cv2.imshow("Original Image", img)
cv2.imshow("Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
