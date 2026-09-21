import cv2

# Open the main camera (video0)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open the camera")
    exit()

print("Camera opened. Press the Q key to quit.")

while True:
    ok, frame = camera.read()
    if not ok:
        print("Could not read the frame")
        break

    cv2.imshow("Camera test - press Q to quit", frame)

    # If Q is pressed, exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
print("Camera closed correctly.")