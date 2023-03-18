import cv2

webcam = cv2.VideoCapture(0)

stop = False


#while this loop is running it is looking for one of two keys to be pressed (s or q). If s is pressed an image will be captured from the webcam if q is pressed the script will end
while stop==False:
    ret,frame = webcam.read()
    nframe = cv2.flip(frame,1)
    if ret==True:
        cv2.imshow("camera", nframe)
        key = cv2.waitKey(1)
        if key==ord("q"):
            stop = True
        if key==ord("s"):
            im_name = "testim.png"
            cv2.imwrite(im_name,nframe)
