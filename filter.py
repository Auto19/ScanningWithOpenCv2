import cv2
import numpy as np


cam = cv2.VideoCapture(0)

lower_blue = np.array([5, 50, 50])
upper_blue = np.array([15, 255, 255])

while True:
  ret, img = cam.read()

  if ret == True:
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      mask = cv2.inRange(hsv, lower_blue, upper_blue)
      cv2.imshow("CAM2", mask)


  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyAllWindows()
    cam.release()
    break

print('Sensor off')
