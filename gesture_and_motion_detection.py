import cv2
import mediapipe as mp
import time
import pyautogui

scr_width, scr_height = pyautogui.size()

pTime=0

# pc cam 
# #cap = cv2.VideoCapture(0)


url = "http://192.168.1.100:8080/video"
cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(20,50),cv2.QT_FONT_BLACK,2,(255,0,255),5,1,0)

    ##print hand location print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                #print(h,w,c)
                cx ,cy = int(lm.x * w), int(lm.y *h)
                #print(id,cx,cy)


                if id==8:
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
                    scr_x = scr_width/w*cx
                    scr_y = scr_height/h*cy
                    pyautogui.moveTo(scr_x, scr_y)


                if id==12:
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)

                    
                #mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)


            
            print("=============================")
    cv2.imshow("Image" ,img)
    cv2.waitKey(1)