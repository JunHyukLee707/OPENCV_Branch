import cv2

def gray(src) :
    dest=cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    return dest
