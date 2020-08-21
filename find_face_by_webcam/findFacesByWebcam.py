import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import numpy as np

# Basic face recognition with Python-OpenCV2
# Don't forget to include cascade files in the project folder


# Code below is for log creation, if you want to create logs, comment out the code block at line 50 and the below one.
# log.basicConfig(filename='webcam.log',level=log.INFO)


# This is our base recognition file, program recognizes faces by looking at this file
# If you want to change the object you want to recognize, change the xml filename by looking at the cascades file
faceCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_alt2.xml")

# This is the initialization for our video souce, if you have multiple cameras, you might want to change the index value (0) 
video_capture = cv2.VideoCapture(0)

# Font for writing text on the screen
font = cv2.FONT_HERSHEY_COMPLEX

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Turning the frame into gray so our cascade file can recognize faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detection funciton
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces (w is for width, h is for height)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    """
    if  len(faces) != 0:
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))"""

    # Writing a text on the frame
    cv2.putText(frame,"Faces found: {}".format(len(faces)),(5,30),font,1,255)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Set the program to close when the key "q" is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()