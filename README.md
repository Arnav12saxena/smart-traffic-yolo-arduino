# 🚦 Smart Traffic Control System using YOLOv8 + Arduino  
### Real-Time Vehicle Detection & Adaptive Traffic Signal Management

This project implements an AI-powered **adaptive traffic light controller** using:

- **YOLOv8 (Ultralytics)** for real-time vehicle detection  
- **IP Webcam** for live video input  
- **Arduino UNO** for controlling traffic LEDs (Red–Yellow–Green)  
- **Python–Arduino serial communication**  
- **Dynamic green-light timing** based on detected traffic density  

The system automatically **increases or decreases green-light duration** depending on the number of vehicles in each frame.

---

# 📌 1. Project Overview

Traditional traffic signals operate on **fixed timers**, causing:

- Long waiting times during low traffic  
- Congestion during peak hours  
- Fuel wastage  
- Increased pollution  

This project solves the problem by building a **smart, adaptive traffic system** that adjusts timings based on real-time vehicle counts using YOLO object detection.

### ✔ Key Features  
- Detects vehicles: **car, truck, bus, motorcycle**  
- Counts total vehicles in each frame  
- Dynamically adjusts green-light duration  
- Communicates timings to Arduino via serial  
- Controls actual **Red, Yellow, Green LEDs**  
- Works with any **IP Webcam or USB camera**  

---

# 🧠 2. System Architecture

**IP Camera → YOLOv8 → Vehicle Count → Dynamic Timing Logic → Arduino Serial → Traffic Lights**

### Components:
- **Python YOLO Script** (`test_camera.py`)
- **Ultralytics YOLOv8**
- **Arduino UNO**
- **Traffic light LEDs: Red, Yellow, Green**
- **Serial USB Cable**

---

# 🗂 3. Dataset & Model

This project uses the **pretrained YOLOv8n COCO model**:

```
yolov8n.pt
```

### COCO Vehicle Class IDs Used:

| Vehicle Type | Class ID |
|--------------|----------|
| Car | 2 |
| Truck | 3 |
| Bus | 5 |
| Motorcycle | 7 |

All YOLO detections are filtered using these IDs.

---

# ⚙️ 4. How the System Works

### ✔ Step 1 — YOLO detects vehicles  
Each live frame is processed using `yolov8n.pt`.

### ✔ Step 2 — Vehicle count extracted  
Counts the number of detected cars, trucks, buses, and motorcycles.

### ✔ Step 3 — Compute adaptive signal timings  
More vehicles ⇒ allocate **longer green time**.

### ✔ Step 4 — Timings sent to Arduino via Serial  
Format:  
```
red_time,yellow_time,green_time
```

### ✔ Step 5 — Arduino switches LEDs  
Traffic lights turn on/off based on received values.

---

# 📦 5. Installation

### Install Python dependencies:
```bash
pip install ultralytics opencv-python pyserial
```

### Run Python detection script:
```bash
python test_camera.py
```

### Upload Arduino Code:
Upload `arduino_traffic_controller.ino` using Arduino IDE  
Select correct **COM port** + **Arduino UNO**

---

# 🛠 6. Hardware Setup (Arduino)

### Required Components:
- Arduino UNO  
- Red LED  
- Yellow LED  
- Green LED  
- 220Ω resistors  
- Jumper wires  
- Breadboard  

### Pin Connections:

| LED | Arduino Pin |
|-----|-------------|
| Red | 13 |
| Yellow | 12 |
| Green | 11 |

---

# 📂 7. Recommended Repository Structure
```
smart-traffic-yolo-arduino/
│── test_camera.py
│── yolov8n.pt
│── arduino_traffic_controller.ino
│── requirements.txt
│
└── README.md
```

---

# 🚀 8. Future Improvements

- Train YOLOv8 on **Indian traffic vehicle dataset**  
- Dual-direction or 4-way signal support  
- Real intersection density-based routing  
- Replace Arduino UNO with **ESP32** (WiFi support)  
- Deploy on **Raspberry Pi** for real-time edge processing  
- Emergency vehicle priority (ambulance detection)  
- License plate recognition integration  

---

# 🏁 9. Conclusion

This project demonstrates a complete **AI + IoT smart traffic system** combining:

- Real-time object detection  
- Dynamic traffic logic  
- Hardware execution with Arduino  
- Efficient serial communication  

It forms a strong foundation for **smart city traffic automation** and scalable intelligent transport systems.

---

# 📬 Contact

**Arnav Saxena**  
🔗 LinkedIn: https://www.linkedin.com/in/arnav-saxena-a9a217367  
📧 Email: **arnav12saxena@gmail.com**
