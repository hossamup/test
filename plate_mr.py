import numpy as np
import cv2

image = cv2.imread("Resources/Scanned/NoPlate_2.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

dst = cv2.Canny(grayImage, 50, 100)

dst = cv2.morphologyEx(dst, cv2.MORPH_RECT, np.zeros((5,5), np.uint8), 
                       iterations=1)
cv2.imwrite("Resources/Scanned/scanned_Mr/canny.jpg", dst)

contours, heirarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(contours)
for i in range(0, len(contours)):
    if cv2.contourArea(contours[i]) > 200:
        x,y,w,h = cv2.boundingRect(contours[i])
        # The w constrain to remove the vertical lines
        if w > 10:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 1)
            cv2.imwrite("Resources/Scanned/scanned_Mr/contour.jpg", image)