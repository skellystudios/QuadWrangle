import cv2
import numpy as np
import serial 
import math
# if you have not already done so

cv2.namedWindow("lll")
cap = cv2.VideoCapture(0)

try:
    ser = serial.Serial('/dev/tty.usbmodem411', 115200)
except:
    print "Not connected to serial"
val = 0
hand_height = 1
start = False
ticker = 0
last_out = 0

while( cap.isOpened() ) :
    ret,img = cap.read()

    height = img.shape[0]


    """
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    (height, width, d) = img.shape

    for h in range(0, height):
        for w in range(0,width):
            out[h,w] = fst(img[h,w,:])



    #cv2.circle(img,(x,y),3,255,-1)
    """

    cascade = cv2.CascadeClassifier("cascades/1256617233-1-haarcascade_hand.xml")
    rects = cascade.detectMultiScale(img, 1.1, 18, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))


    top_hand = height

    if len(rects) != 0:
        rects[:, 2:] += rects[:, :2]
    
    for x1, y1, x2, y2 in rects:
        if y2<top_hand:
            top_hand = y2
            hand_height = max(y2-y1,1)
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)

    if len(rects) != 0:
        val = top_hand
    else:
        val = 0



    out = (height - val)/float(height - hand_height) * 255 
    if val == 0: out = 0
    #print '%03d' % out
    #print "height %s hand height %s val %s" % (height, hand_height, out)

    out = max(min(out,255),0)
    out2 = math.floor(out/10)
    out = out2 * 10

    cv2.putText(img, '%03d' % out, (90,90), 2, 3, 3);
    
    ticker = ticker + 1

    if start and (ticker > 2) and (out != last_out):
        ticker = 0    
        print '%03d' % out
        ser.write('%03d' % out)
        last_out = out

    cv2.imshow("lll",img)
    k = cv2.waitKey(10)
    if k == 27:
        break
    if k == 32:
        start = True
