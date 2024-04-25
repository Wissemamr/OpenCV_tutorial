import cv2 as cv


# reading and resizing an image
red_parrot_img = cv.imread('figs\\red_parrot.png')
resized_red_parrot_img = cv.resize(red_parrot_img, (700, 500))
cv.imshow('Red Parrot', resized_red_parrot_img)
cv.waitKey(0)


# reading videos
# O for webcam
cap = cv.VideoCapture('figs\\maroon5_maps.mp4')
while True : 
    isTrue, frame = cap.read()
