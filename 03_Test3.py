import serial
import time
import qrcode
import cv2

kochi = ['1004', '1005']
kottayam = ['1006', '1007']

serialPort = serial.Serial(
    port="COM6", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
d = cv2.QRCodeDetector()
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN


def get_destination(id):
    dest = "unknown"
    id = int(id)
    for i in kottayam:
        if int(i) == id:
            dest = "Kottayam"
            return dest

    for i in kochi:
        if int(i) == id:
            dest = "Cochin"
            return dest
    return dest


x = input("press 1 to begin")
msg_dest = "unknown"
while True:
    if x == '1':
        serialPort.write(b"a\r\n")
        x = 0
    _, frame = cap.read()
    val, points, straight_qrcode = d.detectAndDecode(frame)
    if val:
        msg_disp = get_destination(val)
        msg_dest = msg_disp
        if int(val) == 1008:
            print ("please restart again")
            serialPort.write(b"sss\r\n")
            break
        val = " ID = " + val
        msg_disp = " Destination = " + msg_disp
        print(val)
        cv2.putText(frame, str(val), (50, 50), font, 2,
                    (255, 0, 0), 2)
        cv2.putText(frame, str(msg_disp), (50, 130), font, 2,
                    (0, 0, 255), 2)

        print(msg_disp)
    cv2.imshow('Frame', frame)

    if msg_dest == "Kottayam":
        cv2.imshow('Frame', frame)
        serialPort.write(b"m\r\n")
        print("Setting dest to Kottayam")
        time.sleep(3)
        serialPort.write(b"d\r\n")
        time.sleep(2)
        print("stop")
        #serialPort.write(b"b\r\n")
        msg_dest = "unknown"

    if msg_dest == "Cochin":
        cv2.imshow('Frame', frame)
        print("Setting dest to Cochin")
        serialPort.write(b"n\r\n")
        time.sleep(3)
        serialPort.write(b"d\r\n")
        time.sleep(2)
        print("stop")
        #serialPort.write(b"b\r\n")
        msg_dest = "unknown"
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
