import cv2
import os

# Folder where captured photos will be saved
OUTPUT_FOLDER = "faces"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Ask for the person's name so photos are labeled
person = input("Person's name (e.g. henry): ").strip().lower()

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Could not open the camera")
    exit()

count = 0
print("Camera ready.")
print("Press SPACE to capture a photo, Q to quit.")

while True:
    ok, frame = camera.read()
    if not ok:
        print("Could not read the frame")
        break

    # Show a helper text on screen
    text = f"{person} | photos: {count} | SPACE=capture  Q=quit"
    cv2.putText(frame, text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Capture faces - SPACE to capture, Q to quit", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord(" "):  # SPACE
        count += 1
        filename = os.path.join(OUTPUT_FOLDER, f"{person}_{count}.jpg")
        cv2.imwrite(filename, frame)
        print("Saved:", filename)

    elif key == ord("q"):  # Q
        break

camera.release()
cv2.destroyAllWindows()
print(f"Done. {count} photos saved in the '{OUTPUT_FOLDER}' folder.")