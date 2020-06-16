import numpy as np
import cv2
import cmath  

fire_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('fire.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dimensions=img.shape
print(dimensions)
fires = fire_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in fires:
    if(w>50 and h>50):
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        c=img.shape[0]-(y+h)
        print(c)
    
a=0.0323
b=22.208
d=(b**2) - (4*a*(1.3132-c))
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print(d)
print(sol1)
print(sol2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()