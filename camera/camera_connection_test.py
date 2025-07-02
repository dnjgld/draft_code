import cv2

# test to open the camera
# cap = cv2.VideoCapture(0)

# try the rtmp stream of IP camera
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('rtsp://128.164.210.220')
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        
# cap.set(propId, value)
# print(cap.isOpened())

while cap.isOpened():
    ret_flag, img_camera = cap.read()

    # print("height: ", img_camera.shape[0])
    # print("width:  ", img_camera.shape[1])
    # print('')

    cv2.imshow("camera", img_camera)

    k = cv2.waitKey(1)
    if k == 27: # press esc
        break

cap.release()
cv2.destroyAllWindows()
