import cv2
import numpy as np

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

# cap.set(propId, value)
# print(cap.isOpened())
if cap.isOpened():
    print("Start")
    ret_flag, img0 = cap.read()

def distance(image, image_to_compare):
    a = np.array(image)
    b = np.array(image_to_compare)
    return np.linalg.norm(a - b)

count=0
remind=False
while cap.isOpened():
    count+=1
    ret_flag, img_camera = cap.read()
    # print("height: ", img_camera.shape[0])
    # print("width:  ", img_camera.shape[1])
    # print('')
    
    if count%100==0:
        cv2.imshow("Camera", img_camera)
        # cv2.imshow("Video", img0)
        # print(distance(img_camera, img0))
        if distance(img_camera, img0)>100000:
            print("Changed")
        elif not remind:
            print("Not Changed")
            remind=True
        img0 = img_camera
        

    k = cv2.waitKey(1)
    if k == 27: # press esc
        break


cap.release()
cv2.destroyAllWindows()
