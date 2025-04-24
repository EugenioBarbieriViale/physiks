from matplotlib.pyplot import imshow, show
import cv2 as cv

# image = cv.imread("t.jpg")
image = cv.imread("test.png")
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# image = cv.Canny(image, 100, 200)
# image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# image = cv.GaussianBlur(image, (5, 5), 0)
# th, image = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# cv.drawContours(image, contours, -1, (0, 255, 0), 2)

imshow(image, cmap="gray")
show()
