import cv2
import easygui
import numpy as np

# gen poly
lx = [0,300,400,500,600,700,800,900,1000]
ly = [538,559,581,604,626,655,677,723,769]
l = np.polyfit(lx, ly, 2)
l = l[::-1]

def pix_f_dist(dist):
    global l
    return sum([c*dist**i for i,c in enumerate(l)])

x_pos = 605


while True:
    ret_img = cv2.imread("MSR_TX5i.jpg")
    en_dist = easygui.enterbox("Range")
    try:
        en_dist = int(en_dist)
    except:
        if en_dist is None:
            exit()
        continue

    y_pos = pix_f_dist(en_dist)
    y_pos = round(y_pos, 0)

    x,y = (int(x_pos),int(y_pos))

    img = cv2.circle(ret_img, (x, y), radius=5, color=(0,255,0), thickness=-1)
    width = int(img.shape[1] * 90 / 100)
    height = int(img.shape[0] * 90 / 100)
    img = cv2.resize(img, (width,height), interpolation = cv2.INTER_AREA)

    cv2.namedWindow("where to shoot")
    cv2.moveWindow("where to shoot",0,0)
    cv2.imshow("where to shoot", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
