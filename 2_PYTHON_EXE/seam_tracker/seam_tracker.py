import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

VIDEO = "./color.mp4"
cap = cv2.VideoCapture(VIDEO)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

while True:
    _,frame = cap.read()
    
    im = cv2.GaussianBlur(frame, (5,5), 1)
    img = im[:,:,2]
    _, img = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)
    
    img = cv2.Canny(img, 20, 200, None, 3)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    lines = cv2.HoughLines(img, 1,  2*np.pi / 180, 80, None, 0, 0)
    #
    list1= []
    list2 = []
    list3 = []
    list4 = []
    
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            list1.append(x0)
            list2.append(y0)
            list3.append(a)
            list4.append(b)
            
        list1 = np.array(list1)
        list2 = np.array(list2)
        list3 = np.array(list3)
        list4 = np.array(list4)
        x0 = list1.mean()
        y0 = list2.mean()
        a = list3.mean()
        b = list4.mean()
        
        pt1 = (int(x0 + 10*(-b)), int(y0 + 10*(a)))
        pt2 = (int(x0 - 10*(-b)), int(y0 - 10*(a)))
        cv2.line(frame, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    
    cv2.imshow('video',frame)
    cv2.imshow('canny', img)
    key = cv2.waitKey(10)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

histg = cv2.calcHist([img2],[0],None,[256],[0,256]) 
plt.plot(histg)
plt.show()