import cv2

# Open the default camera (usually 0)
cap = cv2.VideoCapture(0)
while(True):
    # Read a frame from the camera
    ret, frame = cap.read()
    cv2.imwrite('test.jpg', frame)

    img = cv2.imread('test.jpg')

    # Display original image
    cv2.imshow('Original', img)
    #cv2.waitKey(0)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # Sobel Edge Detection
    #sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Sobel Edge Detection on the X axis
    #sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)  # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)  # Combined X and Y Sobel Edge Detection
    # Display Sobel Edge Detection Images
    #cv2.imshow('Sobel X', sobelx)
    #cv2.waitKey(0)
    #cv2.imshow('Sobel Y', sobely)
    #cv2.waitKey(0)
    cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    #cv2.waitKey(0)

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=50, threshold2=200)  # Canny Edge Detection
    # Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)
    #cv2.waitKey(0)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

