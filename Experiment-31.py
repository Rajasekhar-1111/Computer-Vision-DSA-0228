import cv2
import numpy as np

# Read image
img = cv2.imread("watch.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur to reduce noise
gray = cv2.GaussianBlur(gray, (9,9), 2)

# Detect circles
circles = cv2.HoughCircles(gray,
                           cv2.HOUGH_GRADIENT,
                           1, 100,
                           param1=100,
                           param2=30,
                           minRadius=50,
                           maxRadius=200)

# Draw detected circle
if circles is not None:
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),3)
        cv2.putText(img,"Watch",(i[0]-40,i[1]-i[2]-10),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

# Display result
cv2.imshow("Watch Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()