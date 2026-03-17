import cv2

# Open the video file
cap = cv2.VideoCapture("video.mp4")

frames = []

# Read all frames and store them
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play frames in reverse order
for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == 27:   # Press ESC to stop
        break

cv2.destroyAllWindows()