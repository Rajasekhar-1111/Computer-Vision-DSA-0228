import cv2

img = cv2.imread("image.jpg")

print("Image size:", img.shape)

# Crop
crop = img[20:80, 20:120]

h, w, _ = crop.shape

# Paste safely inside image
img[60:60+h, 20:20+w] = crop

cv2.imshow("Cropped", crop)
cv2.imshow("Result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()