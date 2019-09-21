"""
Created by: Rishikesh Vanarse
20/09/19
"""

import cv2
import numpy as np


#Single Green tag detection + tracking through multiple frames

feed = cv2.VideoCapture(0)

while(1):
	#Get frame
	ret, frame = feed.read()

	#Show original
	cv2.imshow('Original Video', frame)

	#Extract Greens
	temp_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	green_param1 = np.array([45, 25, 25])
	green_param2 = np.array([86, 255, 255])
	temp_img = cv2.inRange(temp_img, green_param1, green_param2)
	temp_img = cv2.blur(temp_img, (13,13))
	ret, temp_img = cv2.threshold(temp_img, 210, 255, cv2.THRESH_BINARY)
	#mask = cv2.inRange(frame, np.array([0 ,100, 0]), np.array([100 ,255,100]))
	#Show result

	img2, contours, hierarchy = cv2.findContours(temp_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cv2.imshow('Intermediate', temp_img)
	img2 = cv2.drawContours(img2, contours, 0, (0,255,0), 1)
	cv2.imshow('Contour', img2)

	#cv2.imshow('Green', cv2.threshold(frame[:,:,0], 200, 255, cv2.THRESH_BINARY)[1])

	#image, contours, hierarchy = cv2.findContours(temp_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	#cv2.imshow('contours', cv2.drawContours(image, contours, -1, (0,255,0), 3))
	#Esc

	moments = cv2.moments(contours[0])
	"""
	rect = cv2.minAreaRect(contours[0])
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	img2 = cv2.drawContours(img2, [box],0,(0,0,255),2)
	cv2.imshow('Bounds', img2)
	"""


	if cv2.waitKey(1)==27:
		break
	
#Cleanup
feed.release()
cv2.destroyAllWindows()

for M in moments:
	print(M, moments[M])