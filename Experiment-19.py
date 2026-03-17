import cv2

# Read image in grayscale
img = cv2.imread('image.jpg', 0)

# Create blurred image using Gaussian Blur
blur = cv2.GaussianBlur(img, (5,5), 0)

# Unsharp masking
sharpened = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()