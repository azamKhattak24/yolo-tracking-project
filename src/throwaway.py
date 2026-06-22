import cv2

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
print("Opened:", cap.isOpened())

ret, frame = cap.read()
print("Frame read:", ret)

if ret:
    cv2.imshow("Test", frame)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
