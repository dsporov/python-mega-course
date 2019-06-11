import cv2

#video = cv2.VideoCapture("movie.mp4")

video = cv2.VideoCapture(0)
while True:
    # boolean flag + 3-dim array
    check, frame = video.read()
    cv2.imshow("Capturing", frame)

    #time.sleep(4)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()
