import cv2

img = cv2.imread("images/ironman.jpeg")
cv2.imshow("Love you 3000", img)

cv2.waitKey(0)
cv2.destroyAllWindows()