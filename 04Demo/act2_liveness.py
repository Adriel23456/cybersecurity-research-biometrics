import cv2
import time
from deepface import DeepFace

MODEL = "ArcFace"
DEFAULT_THRESHOLD = 0.68  # ArcFace default threshold

# Reference photo: the "enrolled" identity the system trusts
REFERENCE = "faces/henry_1.jpg"

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Could not open the camera")
    exit()

print("Live camera running.")
print("Controls: W = raise threshold, S = lower threshold, D = back to default, Q = quit")

threshold = DEFAULT_THRESHOLD
last_check = 0.0
check_every = 1.0  # seconds between comparisons
current_distance = None

while True:
    ok, frame = camera.read()
    if not ok:
        break

    now = time.time()

    # Run the heavy comparison once per second
    if now - last_check >= check_every:
        last_check = now
        try:
            result = DeepFace.verify(
                img1_path=REFERENCE,
                img2_path=frame,  # current camera frame
                model_name=MODEL,
                enforce_detection=False,
            )
            current_distance = result["distance"]
        except Exception:
            current_distance = None

    # Decide using the CURRENT threshold (which the user can move)
    if current_distance is not None:
        is_match = current_distance < threshold
        label = "MATCH: Henry" if is_match else "NO MATCH"
        color = (0, 255, 0) if is_match else (0, 0, 255)
        line1 = f"{label}  |  distance: {round(current_distance, 3)}"
    else:
        color = (0, 255, 255)
        line1 = "Looking for a face..."

    line2 = f"threshold: {round(threshold, 2)}   (W=up  S=down  D=default)"

    cv2.putText(frame, line1, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    cv2.putText(frame, line2, (10, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.imshow("Live demo - threshold and presentation attack (Q to quit)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("w"):
        threshold = min(threshold + 0.05, 1.5)  # raise
    elif key == ord("s"):
        threshold = max(threshold - 0.05, 0.0)  # lower
    elif key == ord("d"):
        threshold = DEFAULT_THRESHOLD  # back to default

camera.release()
cv2.destroyAllWindows()