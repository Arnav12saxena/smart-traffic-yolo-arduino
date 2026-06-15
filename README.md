# 🚦 Smart Traffic Control System Using YOLOv8 + Arduino

### AI-Powered Real-Time Vehicle Detection · Adaptive Traffic Signal Prioritization · Computer Vision + IoT Integration

This project presents an intelligent traffic management system that uses real-time vehicle detection powered by YOLOv8 to dynamically prioritize traffic flow at an intersection.

The system monitors traffic density using computer vision and automatically controls two Arduino-based traffic signal modules. When congestion exceeds a predefined threshold, the system grants signal priority to the congested road, demonstrating adaptive traffic control instead of traditional fixed-time signaling.

It integrates:

* Computer Vision (YOLOv8)
* Real-Time Vehicle Detection
* Python → Arduino Serial Communication
* Intelligent Traffic Prioritization
* IoT Hardware Control
* Live Video Inference

A complete AI + IoT prototype designed for next-generation smart traffic infrastructure.

---

# 📌 Introduction

Traditional traffic lights operate using fixed timers regardless of actual traffic conditions. This often leads to:

* Unnecessary waiting times
* Traffic congestion
* Fuel wastage
* Increased emissions
* Poor traffic flow efficiency

To address this issue, this project introduces an AI-driven traffic management system that continuously analyzes traffic density and dynamically allocates signal priority.

Using YOLOv8, vehicles are detected and counted in real time from a live camera feed. Based on the detected traffic density, the system automatically decides which road receives priority and updates the physical traffic lights through an Arduino Uno.

---

# 🎯 Project Objectives

✔ Detect vehicles in real time using YOLOv8

✔ Count traffic density from a live camera feed

✔ Classify traffic as normal or congested

✔ Implement adaptive traffic signal control

✔ Control physical traffic lights using Arduino

✔ Demonstrate Computer Vision + IoT integration

✔ Simulate intelligent intersection management

---

# 🧠 System Architecture

Camera Feed (Road A)
↓
YOLOv8 Vehicle Detection
↓
Vehicle Counting
↓
Traffic Density Analysis
↓
Decision Engine
↓
Python → Arduino Communication
↓
Traffic Signal Control
↓
Road A / Road B Priority Assignment

---

# ⚙️ How the System Works

## Step 1: Vehicle Detection

The camera continuously monitors Road A.

YOLOv8 detects:

* Cars
* Motorcycles
* Buses
* Trucks

in every frame.

---

## Step 2: Vehicle Counting

Detected vehicles are counted to estimate traffic density.

Example:

Vehicle Count = 3

Vehicle Count = 15

Vehicle Count = 28

---

## Step 3: Intelligent Decision Making

A congestion threshold is defined.

Example:

Threshold = 10 Vehicles

Decision Logic:

If Vehicle Count ≥ 10

→ Road A receives priority

If Vehicle Count < 10

→ Road B receives priority

---

## Step 4: Signal Control

Road A Priority:

* Road A → GREEN
* Road B → RED

Road B Priority:

* Road A → RED
* Road B → GREEN

The decision is transmitted from Python to Arduino using serial communication.

---

# 🔌 Hardware Setup

## Traffic Light A (Road A)

* Red → Pin 13
* Yellow → Pin 12
* Green → Pin 11

## Traffic Light B (Road B)

* Red → Pin 10
* Yellow → Pin 9
* Green → Pin 8

## Components

* Arduino Uno
* 2 Traffic Light Modules
* Android IP Webcam
* YOLOv8n Model
* Python
* OpenCV
* PySerial

---

# 📊 Results

✔ Real-time vehicle detection

✔ Adaptive traffic prioritization

✔ Automatic signal switching

✔ Stable Arduino communication

✔ AI-driven decision making

✔ Complete Computer Vision → IoT → Hardware workflow

---

# 🚀 Future Enhancements

### AI Improvements

* Custom-trained traffic models
* Vehicle tracking using DeepSORT
* Lane-specific vehicle counting
* Speed estimation

### Hardware Improvements

* Multiple cameras
* Multi-intersection deployment
* ESP32 wireless communication
* Raspberry Pi edge inference

### Smart City Features

* Emergency vehicle prioritization
* Traffic analytics dashboard
* Route optimization
* Cloud-based monitoring

---

# 🏁 Conclusion

This project demonstrates how Artificial Intelligence and IoT can be combined to build adaptive traffic management systems.

Using YOLOv8 for real-time vehicle detection and Arduino-controlled traffic signals, the system dynamically prioritizes traffic flow based on congestion levels.

The project serves as a practical prototype for intelligent transportation systems and smart-city infrastructure.
