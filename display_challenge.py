import cv2 

# display image
img = cv2.imread("Photos\space_image.jpg")
cv2.imshow('Space Image', img)
cv2.waitKey(0)

# display video
vid = cv2.VideoCapture("Photos\space_video.mp4")

while True:
    frame = vid.read()[1]
    cv2.imshow('Space Video', frame)

    # close screen when q is pressed
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

vid.release()
