import serial
from ultralytics import YOLO
import cv2
import time

# -----------------------------
# Connect to Arduino
# -----------------------------
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to initialize

# -----------------------------
# Load YOLO model
# -----------------------------
model = YOLO('yolov8n.pt')  # or your trained model

# -----------------------------
# Open IP webcam feed
# -----------------------------
cap = cv2.VideoCapture('http://192.168.1.32:8080/video')

# -----------------------------
# Main loop
# -----------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        continue

    # YOLO detection
    results = model(frame)

    # Filter vehicle classes: car(2), truck(3), bus(5), motorcycle(7)
    vehicle_boxes = [box for i, box in enumerate(results[0].boxes) if int(results[0].boxes.cls[i]) in [2, 3, 5, 7]]
    vehicle_count = len(vehicle_boxes)

    # Draw bounding boxes on frame
    for box in vehicle_boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display vehicle count on frame
    cv2.putText(frame, f"Vehicles: {vehicle_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Traffic Feed", frame)

    # Determine traffic light timings
    green_time = 3000 + vehicle_count * 1000  # base 3s + 1s per vehicle
    red_time = 5000
    yellow_time = 2000

    # Send command to Arduino
    command = f"{red_time},{yellow_time},{green_time}\n"
    arduino.write(command.encode())

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()
