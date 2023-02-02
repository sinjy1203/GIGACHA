import cv2
import sys

# Load Web Camera
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 3) # auto mode
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1) # manual mode
cap.set(cv2.CAP_PROP_EXPOSURE, -11) # -1 to -13
if not (cap.isOpened()):
    print("File isn't opend!!")

# Set Video File Property
videoFileName = 'video/output42.avi'
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # width
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # height
fps = cap.get(cv2.CAP_PROP_FPS)  # frame per second
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # fourcc
delay = round(1000 / fps)  # set interval between frame

# Save Video
out = cv2.VideoWriter(videoFileName, fourcc, fps, (w, h))
if not (out.isOpened()):
    print("File isn't opend!!")
    cap.release()
    sys.exit()

# Load frame and Save it
while (True):  # Check Video is Available
    ret, frame = cap.read()  # read by frame (ret=TRUE/FALSE)s

    if ret:
        out.write(frame)  # save video frame

        cv2.imshow('Original VIDEO', frame)

        if cv2.waitKey(delay) == 27:  # wait 10ms until user input 'esc'
            break
    else:
        print("ret is false")
        break

cap.release()  # release memory
out.release()  # release memory
cv2.destroyAllWindows()  # destroy All Window