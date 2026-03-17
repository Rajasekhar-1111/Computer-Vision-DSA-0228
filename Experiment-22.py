import cv2

# Read the original image
img = cv2.imread("image.jpg")

# Watermark text
text = "WATERMARK"

# Position of watermark
position = (50, 50)

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX

# Add watermark text to image
cv2.putText(img, text, position, font, 1, (255,255,255), 2)

# Display image
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()