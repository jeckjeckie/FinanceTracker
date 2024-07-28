import cv2 as cv

foto = cv.imread("a.jpeg")
cv.rectangle(foto,(20,10),(200,200),(0,140,155),5)
cv.imshow("window",foto)
cv.waitKey(0)


