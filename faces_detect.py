import cv2

img = cv2.imread('4f.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)
print(len(faces))

for (x,y,l,a) in faces:
    cv2.rectangle(img, (x,y), (x+l, y+a), (255,0,0), 2)

cv2.imshow('Faces detectadas',img)
cv2.waitKey(0)


