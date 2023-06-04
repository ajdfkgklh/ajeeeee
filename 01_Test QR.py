#   pip install qrcode
#   pip install opencv-python
#   pip install pyserial



import qrcode
import cv2


d = cv2.QRCodeDetector()
cap = cv2.VideoCapture(1)
font = cv2.FONT_HERSHEY_PLAIN
while True:
    _, frame = cap.read()
    val, points, straight_qrcode = d.detectAndDecode(frame)
    if val:
        print(val)
        cv2.putText(frame, str(val), (50, 50), font, 2,
                    (255, 0, 0), 1)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
