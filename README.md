![An example](https://i.ibb.co/zht9YZ6/imgonline-com-ua-twotoone-Wh-CJu03i-Gkpe-Y8-KE.jpg)
# Face Recognition with Python and openCV2
 Basic face recognition examples with python and openCV 2
 
 ## Required Libraries
 Required libraries are
```
 os
 numpy
 cv2 (OpenCv2)
```
 
 ## Examples
 
### 1 - Find faces by photo

This program takes a single image file and marks the faces on it. Then shows it to the user.
####

### 2 - Find faces by webcam

This program takes live input from user's webcam and marks faces on it.

### 3 - Extract images

This program takes image/images from the user and marks the faces. Then it saves both the full and the cropped image in a new folder. You can copy multiple folders into the images folder. Just be careful to not copy empty folders. Folder creation is handled by the program.

## Possible Modifications
- Any user can change the cascade classifier (xml file) and idenify any object they want.
- User can create his/her own cascade classifier by creating and training a dataset. A great and useful guide to creating a cascade classifier can be found [here](https://medium.com/@toshyraf/train-dataset-to-xml-file-for-cascade-classifier-opencv-43a692b74bfe).
