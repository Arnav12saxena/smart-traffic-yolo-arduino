import serial
from ultralytics import YOLO
import cv2
import time

# -----------------------------
# Arduino Connection
# -----------------------------
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

# -----------------------------
# Load YOLO Model
# -----------------------------
model = YOLO("yolov8n.pt")

# -----------------------------
# IP Webcam
# -----------------------------
cap = cv2.VideoCapture("http://192.168.1.18:8080/video")

# -----------------------------
# Variables
# -----------------------------
last_send = 0
send_interval = 3  # seconds

current_state = None

# -----------------------------
# Main Loop
# -----------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        continue

    # YOLO Detection
    results = model(frame)

    vehicle_boxes = []

    for i, cls in enumerate(results[0].boxes.cls):

        class_id = int(cls)

        # COCO vehicle classes
        if class_id in [2, 3, 5, 7]:
            vehicle_boxes.append(results[0].boxes[i])

    vehicle_count = len(vehicle_boxes)

    # -----------------------------
    # Draw Boxes
    # -----------------------------
    for box in vehicle_boxes:

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

    # -----------------------------
    # Decision Logic
    # -----------------------------
    if vehicle_count >= 10:
        desired_state = "A"
        status_text = "Road A Priority"

    else:
        desired_state = "B"
        status_text = "Road B Priority"

    # -----------------------------
    # Send only when state changes
    # -----------------------------
    current_time = time.time()

    if (
        desired_state != current_state
        and current_time - last_send > send_interval
    ):

        arduino.write(f"{desired_state}\n".encode())

        print(
            f"Vehicles={vehicle_count} "
            f"-> {status_text}"
        )

        current_state = desired_state
        last_send = current_time

    # -----------------------------
    # Display Info
    # -----------------------------
    cv2.putText(
        frame,
        f"Vehicles: {vehicle_count}",
        (10, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        status_text,
        (10, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    # -----------------------------
    # Show Frame
    # -----------------------------
    cv2.imshow("Smart Traffic Control", frame)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()
arduino.close()
