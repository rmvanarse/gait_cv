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

	#Esc
	if cv2.waitKey(1)==27:
		break
	
#Cleanup
feed.release()
cv2.destroyAllWindows()