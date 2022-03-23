import random
import numpy as np
import cvzone as cz
import cv2 
import math
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


detector = HandDetector(detectionCon=0.8, maxHands=1)

class SnakeGameClass:
    def __init__(self,pathFood) -> None:
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.score = 0
        self.points = [] # list of all points of the snake
        self.lengths = [] # distace b/w each point
        self.currentLength = 0 # total length of the snake
        self.allowedLength = 150 # threshold value for the current length
        self.previousHead = 0, 0 # previous head point
        self.imgFood = cv2.imread(pathFood,cv2.IMREAD_UNCHANGED)
        self.hFood,self.wFood,_ = self.imgFood.shape
        self.foodPoints = 0,0
        self.randomFoodLocation()
        self.gameOver = False

    def randomFoodLocation(self):
        self.foodPoints = random.randint(100,1000), random.randint(100,600)
    

    def reduce(self):
        for i, length in enumerate(self.lengths):
            self.currentLength -= length
            self.lengths.pop(i)
            self.points.pop(i)
            if self.currentLength < self.allowedLength: break
    

    def update(self,imgMain,currentHead):
        if self.gameOver:
            cz.putTextRect(imgMain,"Game Over",[300,400],scale=7,thickness=5,offset=20)
            cz.putTextRect(imgMain,f"Your Score: {self.score}",[300,550],scale=7,thickness=5,offset=20)
            # cz.putTextRect(imgMain,"Press R to start",[300,200],scale=7,thickness=2,offset=20)
            # inp = input()
            # if inp.lower() == 'r':
            #     self.gameOver = False
        else:
            cv2.putText(imgMain,str(self.score),(10,500), self.font, 4, (255, 255, 255), 2, cv2.LINE_AA)
            px,py = self.previousHead
            cx,cy = currentHead
            self.points.append([cx,cy])
            distance = math.hypot(cx-px,cy-py)
            self.lengths.append(distance)
            self.currentLength += distance
            self.previousHead = cx,cy

            # length reduction
            if self.currentLength > self.allowedLength:
                self.reduce()

            # check if snake ate the our 🍩🍩
            rx,ry = self.foodPoints
            if rx-self.wFood//2 < cx < rx+self.wFood//2 and ry-self.hFood//2 < cy < ry+self.hFood//2:
                self.randomFoodLocation()
                self.allowedLength += 10
                self.score += 1
            
        

            # Draw Snake
            if self.points:
                for i,point in enumerate(self.points):
                    if i != 0:
                        cv2.line(imgMain,self.points[i-1],self.points[i],(0,0,255),20)
                cv2.circle(imgMain,self .points[-1],20,(200,0,200),cv2.FILLED)
            
            # Draw Food
            imgMain = cz.overlayPNG(imgMain, self.imgFood,(rx-self.wFood//2,ry-self.hFood//2))

            #check for collision
            pts = np.array(self.points[:-2],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(imgMain, [pts],False,(0,200,0),3)
            minimumDistance = cv2.pointPolygonTest(pts,(cx,cy),True)
            if -1 <= minimumDistance <= 1 :
                self.gameOver = True
                self.score = 0
                self.points = []
                self.lengths = [] 
                self.currentLength = 0 
                self.allowedLength = 150 
                self.previousHead = 0, 0 

            return imgMain
    
    

#built the game
game = SnakeGameClass("./Donut.png")
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img,flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        img = game.update(img,pointIndex)
    cv2.imshow('Image',img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        game.gameOver = False
