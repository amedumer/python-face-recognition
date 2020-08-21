import os
import numpy as np
import cv2
import time
# Takes image files from images folder and saves found objects under new foler
face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_alt2.xml")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

for root,dirs,files in os.walk(image_dir):

	label = os.path.basename(root).replace(" ","-").lower()

	if len(files) != 0:
		for file in files:
			if file.endswith("png") or file.endswith("jpg"):
				path = os.path.join(root,file)

				out_path = root[len(BASE_DIR) + 1 ::]
				img_path = path[len(BASE_DIR) + 1 ::]

				imgFile = cv2.imread(img_path)

				new_root = out_path + "\\" + label + "_out"
				
				try:
					os.makedirs(new_root + "_onlyFace")
				except:
					pass

				try:
					os.makedirs(new_root)
				except:
					pass

				faces = faces = face_cascade.detectMultiScale(
						imgFile,
						scaleFactor=1.1,
						minNeighbors=5,
						)

				counter = 0

				for (x,y,w,h) in faces:
					out_faces = out_path + "\\{}_out_onlyFace\\".format(label) + file[0:file.find(".")] + "-" +str(counter) + file[file.find("."):]
					print("Created file: {}".format(out_faces))
					cv2.imwrite(out_faces,imgFile[y:y+h,x:x+w])

					cv2.rectangle(imgFile, (x, y), (x+w, y+h), (255,0,0), 3)
					counter += 1
					

				out = out_path + "\\{}_out\\".format(label) + file
				print("Created file: {}".format(out))
				
				cv2.imwrite(out,imgFile)

print("Process done!")				
				
				
					

