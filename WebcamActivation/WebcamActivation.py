import cv2

camera = cv2.VideoCapture(0) # Selection of camera

while True:
    # val: Validation of camera or video is available.
    # frame: The actual video or camera display in a numpy array.
    val, frame = camera.read()
    cv2.imshow("frame", frame) # Shows movie or video capture
    # Exit the video by pressing 'e'
    if cv2.waitKey(1) == ord("e"):
        break

if __name__ == "__main__":
    # Release the device from the program, making it available to the os again.
    camera.release()
    cv2.destroyAllWindows() # Terminates the video display

