import numpy as np
import cvzone as cz
import cv2 
import math
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

## 
# !!TODO: Built this game more fun 😁
##
detector = HandDetector(detectionCon=0.8, maxHands=1)

class DrawShape:
    def __init__(self) -> None:
        self.points = [] # list of all points of the snake
        self.lengths = [] # distace b/w each point
        self.currentLength = 0 # total length of the snake
        self.allowedLength = 150 # threshold value for the current length
        self.previousHead = 0, 0 # previous head points

    def update(self,imgMain,currentHead):
        px,py = self.previousHead
        cx,cy = currentHead
        self.points.append([cx,cy])
        distance = math.hypot(cx-px,cy-py)
        self.lengths.append(distance)
        self.currentLength += distance
        self.previousHead = cx,cy

        # Draw Shape
        for i,point in enumerate(self.points):
            if i != 0:
                cv2.line(imgMain,self.points[i-1],self.points[i],(0,0,255),20)
        cv2.circle(imgMain,self.points[-1],20,(200,0,200),cv2.FILLED)
        return imgMain

#built the game
game = DrawShape()
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img,flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        img = game.update(img,pointIndex)
    cv2.imshow('Image',img)
    cv2.waitKey(1)