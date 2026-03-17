import cv2

# Read image
img = cv2.imread("image.jpg")

# Coordinates of rectangle
x, y, w, h = 100, 100, 200, 150

# Draw rectangle on image
cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

# Extract object inside rectangle
object_region = img[y:y+h, x:x+w]

# Display images
cv2.imshow("Image with Rectangle", img)
cv2.imshow("Extracted Object", object_region)

cv2.waitKey(0)
cv2.destroyAllWindows()