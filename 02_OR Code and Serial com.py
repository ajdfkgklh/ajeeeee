

import serial
import time
import qrcode
import cv2

kochi = ['1004', '1007', '1005']
kottayam = ['1003', '1008', '1006']


serialPort = serial.Serial(
    port="COM9", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
d = cv2.QRCodeDetector()
cap = cv2.VideoCapture(1)
font = cv2.FONT_HERSHEY_PLAIN

def get_destination(id):
    dest = "unknown"
    id = int(id)
    for i in kottayam:
        if int(i) == id:
            cv2.putText(frame, str("Kottayam"), (50, 130), font, 2,
                        (0, 0, 255), 2)
            dest = "Kottayam"
            cv2.imshow('Frame', frame)
            cv2.imshow('Frame', frame)
            serialPort.write(b"b\r\n")
            time.sleep(5)
            serialPort.write(b"d\r\n")
            serialPort.write(b"a\r\n")
            return dest

    for i in kochi:
        if int(i) == id:
            cv2.putText(frame, str("Cochin"), (50, 130), font, 2,
                        (0, 0, 255), 2)
            dest = "Cochin"
            serialPort.write(b"b\r\n")
            cv2.imshow('Frame', frame)
            cv2.imshow('Frame', frame)
            time.sleep(5)
            serialPort.write(b"d\r\n")
            serialPort.write(b"a\r\n")
            return dest
    return dest

x = input("press 1 to begin")

while True:
    if x == '1':
        serialPort.write(b"a\r\n")
        x = 0
    _, frame = cap.read()
    val, points, straight_qrcode = d.detectAndDecode(frame)
    if val:
        msg_disp = get_destination(val)
        val = " ID = " + val
        msg_disp = " Destination = " + msg_disp
        print(val)
        cv2.putText(frame, str(val), (50, 50), font, 2,
                    (255, 0, 0), 2)
        cv2.putText(frame, str(msg_disp), (50, 130), font, 2,
                    (0, 0, 255), 2)


        print(msg_disp)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break



