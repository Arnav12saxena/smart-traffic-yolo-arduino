# 🚦 Smart Traffic Control System Using YOLOv8 + Arduino  
### AI-Powered Real-Time Vehicle Detection · Adaptive Traffic Signal Optimization · Computer Vision + IoT Integration

This project presents an intelligent traffic management system that dynamically adjusts traffic signal timings using **real-time vehicle detection** powered by YOLOv8, along with hardware-level execution through an **Arduino-driven LED traffic light system**.

It integrates:

- **Computer Vision (YOLOv8)**
- **Python → Arduino Serial Communication**
- **Adaptive Signal Timing Algorithms**
- **IoT Hardware Control**
- **Live Video Inference**

A complete **AI + IoT pipeline** designed for smart city infrastructure.

---

# 📌 1. Introduction

Traditional traffic lights operate on **fixed timers**, resulting in:

- Long waiting times during low-traffic periods  
- Congestion during peak hours  
- Fuel wastage and increased emissions  
- Inefficient traffic flow  

A smart city requires **adaptive, real-time traffic systems**.

This project solves the issue using:

### ✔ YOLOv8 for automatic vehicle detection  
### ✔ Dynamic computation of green-light duration  
### ✔ Arduino-controlled physical LEDs  
### ✔ Real video feed (IP webcam or CCTV)

The system intelligently adjusts signal timings based on real-time vehicle density.

---

# 🎯 2. Project Objectives

- ✔ Real-time vehicle detection using YOLOv8  
- ✔ Count vehicles in each video frame  
- ✔ Calculate signal timings based on density  
- ✔ Send timings to Arduino via serial communication  
- ✔ Physically control R–Y–G LEDs  
- ✔ Demonstrate complete CV → IoT → Hardware workflow  
- ✔ Support any camera input  

---

# 🧠 3. System Architecture

```
Camera Feed
      ↓
YOLOv8 Vehicle Detection (Python)
      ↓
Vehicle Count
      ↓
Adaptive Timing Algorithm
      ↓
Serial Communication (USB)
      ↓
Arduino UNO
      ↓
LED Traffic Lights (Red–Yellow–Green)
```

### Components

- **YOLOv8n (COCO pretrained)**
- **Python (Ultralytics, OpenCV, PySerial)**
- **Arduino UNO**
- **LED traffic light prototype**
- **Android IP Webcam App / USB Camera**

---

# 🗂 4. Detection Model (COCO YOLOv8n)

This system uses the **YOLOv8n** model trained on COCO (80 classes).

### 🚘 Vehicle classes selected:

| Vehicle Type | COCO ID | Used? |
|--------------|---------|--------|
| Car | 2 | ✔ |
| Motorcycle | 3 | ✔ |
| Bus | 5 | ✔ |
| Truck | 7 | ✔ |

These are the most common vehicles in Indian traffic.

---

# ⚙️ 5. How the System Works (Step-by-Step)

## 🔹 Step 1 — Video Capture
```python
cap = cv2.VideoCapture("http://<your-ip>:8080/video")
```

---

## 🔹 Step 2 — YOLOv8 Vehicle Detection
```python
results = model(frame)
vehicle_boxes = [
    box for i, box in enumerate(results[0].boxes)
    if int(results[0].boxes.cls[i]) in [2, 3, 5, 7]
]
```

---

## 🔹 Step 3 — Vehicle Count → Green Time
```python
green_time = 3000 + vehicle_count * 1000
```

Examples:  
- 0 vehicles → **3 seconds** green  
- 5 vehicles → **8 seconds** green  

---

## 🔹 Step 4 — Send Signal Durations to Arduino
```python
command = f"{red_time},{yellow_time},{green_time}\n"
arduino.write(command.encode())
```

---

## 🔹 Step 5 — Arduino Controls LEDs

Arduino cycles:

1. Red  
2. Yellow  
3. Green  

Each according to durations received from Python.

---

# 🔌 6. Arduino Hardware Implementation

### LED Wiring

| LED Color | Arduino Pin |
|-----------|-------------|
| Red | 13 |
| Yellow | 12 |
| Green | 11 |

### Arduino Logic
- Read serial input  
- Parse `"red,yellow,green"` values  
- Control LEDs using `digitalWrite()`  
- Use `delay()` based on timings  

---

# 🧪 7. Python YOLO Script (`test_camera.py`)

Handles:

- YOLOv8 inference  
- Frame capture  
- Detection & counting  
- Timing calculations  
- Box drawing  
- Serial communication  
- Displaying real-time output  

### Dependencies:
- ultralytics  
- opencv-python  
- pyserial  

---

# 🔧 8. Installation & Setup

### Install Python dependencies
```bash
pip install ultralytics opencv-python pyserial
```

### Upload Arduino code
- Open Arduino IDE  
- Select correct **COM port**  
- Upload `arduino_traffic_controller.ino`  

### Run the detection script
```bash
python test_camera.py
```

---

# 📁 9. Recommended Project Structure

```
smart-traffic-yolo-arduino/
│── test_camera.py
│── arduino_traffic_controller.ino
│── yolov8n.pt
│── requirements.txt
└── README.md

```

---

# 📊 10. Results & Demo

✔ Real-time detection at **15–30 FPS**  
✔ Robust identification of cars, bikes, buses, trucks  
✔ Stable serial communication  
✔ Dynamic timing works reliably  
✔ LEDs controlled accurately  
✔ Full AI → IoT → Hardware prototype demonstrated  

**Screenshots/video recommended inside `/media`.**

---

# 🚀 11. Future Enhancements

### 🔵 ML Improvements
- Train YOLO on Indian traffic dataset  
- Add vehicle tracking (DeepSORT)  
- Add speed estimation  

### 🔴 IoT & Hardware Improvements
- Use ESP32 for wireless control  
- Use Raspberry Pi for edge inference  
- Solar-powered smart signal poles  

### 🟨 Additional Features
- Emergency vehicle priority  
- Multi-intersection network  
- Cloud-based analytics dashboard  
- Route optimization using density heatmaps  

---

# 🏁 12. Conclusion

This project demonstrates how **real-time AI + IoT hardware** can significantly improve traffic efficiency.

It successfully integrates:

- Computer Vision  
- Embedded Systems  
- Adaptive Algorithms  
- Serial Communication  
- Practical Hardware Execution  

A strong foundation for **next-generation smart city traffic management** systems.

---

# 📬 Contact

**Arnav Saxena**  
AI/ML · Computer Vision · Embedded Systems  
📧 Email: **arnav12saxena@gmail.com**  
🔗 LinkedIn: https://www.linkedin.com/in/arnav-saxena-a9a217367  
