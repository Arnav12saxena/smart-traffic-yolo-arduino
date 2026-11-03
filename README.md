# 🚦 Smart Traffic Control System Using YOLOv8 + Arduino

### AI-Powered Real-Time Vehicle Detection · Adaptive Traffic Signal Prioritization · Computer Vision + IoT Integration

This 2025 prototype uses a **pretrained YOLOv8n model** to detect and count vehicles in a live camera feed covering **one road (Road A)**. A simple threshold-based rule then selects which of two roads receives priority: when the detected count on Road A is at least 10, Road A receives priority; otherwise, Road B receives priority. Python sends the decision to an Arduino Uno that controls two physical traffic-light modules.

This is a two-road priority demonstration—not lane-wise density estimation or a multi-camera, multi-intersection traffic-management system.

It integrates:

* Computer Vision (YOLOv8)
* Real-Time Vehicle Detection
* Python → Arduino Serial Communication
* Intelligent Traffic Prioritization
* IoT Hardware Control
* Live Video Inference

A small-scale AI + IoT prototype demonstrating vehicle detection, threshold-based priority selection, and physical signal control.

---

# 📌 Introduction

Traditional traffic lights operate using fixed timers regardless of actual traffic conditions. This often leads to:

* Unnecessary waiting times
* Traffic congestion
* Fuel wastage
* Increased emissions
* Poor traffic flow efficiency

To explore a camera-driven alternative, this prototype counts vehicles in a live feed from one road. It uses a fixed threshold of 10 vehicles to choose between Road A and Road B, then updates the two physical traffic-light modules through an Arduino Uno.

---

# 🎯 Project Objectives

✔ Detect vehicles in real time using YOLOv8

✔ Count vehicles in the monitored Road A camera feed

✔ Classify traffic as normal or congested

✔ Apply a fixed-threshold, two-road priority rule

✔ Control physical traffic lights using Arduino

✔ Demonstrate Computer Vision + IoT integration

✔ Demonstrate a small-scale two-road signal-control prototype

---

# 🧠 System Architecture

Camera Feed (Road A)
↓
Pretrained YOLOv8n Vehicle Detection
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

Example vehicle counts are evaluated from the monitored Road A feed.

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

This project demonstrates a basic computer-vision-to-hardware workflow: pretrained YOLOv8n detects vehicles in one road feed, a 10-vehicle threshold selects Road A or Road B priority, and Python communicates the decision to an Arduino Uno. It is an educational prototype rather than a validated city-scale traffic-control system.
