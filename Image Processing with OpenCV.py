#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2

# Load image
image = cv2.imread('your_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

