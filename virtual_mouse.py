import cv2
import mediapipe as mp
import time 
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

index_y =0
pTime =0
cTime =0
while True:
    success, frame = cap.read()
    frame = cv2.flip(frame,1)

    frame_h,frame_w,_ = frame.shape

    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
        
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_w)                    
                y = int(landmark.y*frame_h)            
                # print(x,y)
                # if id == 5:
                #     cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    
                #     palm_x = screen_w / frame_w*x
                #     palm_y = screen_h / frame_h*y

                #     pyautogui.moveTo(palm_x, palm_y)

                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    
                    index_x = screen_w / frame_w*x
                    index_y = screen_h / frame_h*y

                    pyautogui.moveTo(index_x,index_y)
                
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    
                    thumb_x = screen_w / frame_w*x
                    thumb_y = screen_h / frame_h*y
                    # print("outside" ,abs(index_x - thumb_x))
                    if abs(index_y - thumb_y) < 55:
                        pyautogui.click()
                        # print('click')
                        # pyautogui.sleep(1)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)),(10,40), cv2.FONT_HERSHEY_PLAIN,3, (255,0,255), thickness=3)


    cv2.imshow('Virtual Mouse',frame)
    cv2.waitKey(1)