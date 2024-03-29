import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg");
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# in case of poor quality of face detection ou can play around with scaleFactor, minNeighbors or both
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

#print type(faces)
#print faces
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
