import cv2
import numpy as np
import time

video_capture = cv2.VideoCapture(1)

while True:
    ret, frame = video_capture.read()
    vet = frame
    ##vet = cv2.GaussianBlur(frame, (15,15), 2) ##
    vet = cv2.blur(frame, (5,5))
    vet = cv2.Canny(vet,100,200)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)
    output = frame

    if(ret==True):
        cv2.imshow('img',frame)
        cv2.imshow('imgEdge', vet)

        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")

            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                rette = np.copy(output[x-10:x+10, x-10:x+10])
                mask = cv2.inRange(rette, [0, 100, 0], [0, 255, 0])

                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

            # show the output image
        cv2.imshow("output", output)

    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
