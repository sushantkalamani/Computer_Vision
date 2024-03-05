import cv2
import time
import os
import HandTrackModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(3, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
# print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

# print(len(overlayList))

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmlist = detector.findPosition(img,draw=True)
    # print(lmlist)

    if len(lmlist)!=0:
        fingers = []

        #Thumb
        if lmlist[tipIds[0]][1] < lmlist[tipIds[0]-1][1]:
                fingers.append(1)
        else:
                fingers.append(0)

        # for fingers
        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-1][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers) 
        totalFin = fingers.count(1)
        # print(totalFin)


        h, w, c = overlayList[totalFin-1].shape
        img[0:h, 0:w] = overlayList[totalFin-1]


        cv2 .putText(img, str(totalFin), (45, 375), cv2.FONT_HERSHEY_PLAIN ,10, (255, 0, 255), 20)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (450, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)