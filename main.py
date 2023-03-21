import cv2
from open1 import gray   #open1.py 파일의 gray() 함수를 가져옴.
from open2 import hsv, binary


# 영상 소스 열기
src = cv2.imread('c:/photo/picture99.jpg')
dst1= gray(src)
dst2= hsv(src)
dst3= binary(src)


## 영상 디스플레이
cv2.imshow('src', src)

# 마무리
cv2.waitKey(0)
cv2.destroyAllWindows()
