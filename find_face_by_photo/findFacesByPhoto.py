import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

# This is our base recognition file, program recognizes faces by looking at this file
# If you want to change the object you want to recognize, change the xml filename by looking at the cascades file
cascPath = "cascades\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# choosing the source image file
imgFile = cv2.imread("abba.png")

# Turning the frame into gray so our cascade file can recognize faces
gray = cv2.cvtColor(imgFile, cv2.COLOR_BGR2GRAY)

# Face detection funciton
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

# Draw a rectangle around the faces (w is for width, h is for height.) 
for (x, y, w, h) in faces:
        cv2.rectangle(imgFile, (x, y), (x+w, y+h), (0, 255, 0), 2)

caption = str(len(faces)) + " Faces Found!"

cv2.imshow(caption, imgFile)
cv2.waitKey(0)


