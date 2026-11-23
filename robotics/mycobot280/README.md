# MyCobot 280 M5 — Cognitive Robotics

Gesture-controlled robotic arm with computer vision, moving toward autonomous learning through reinforcement learning.

## Scripts

| File | Description |
|------|-------------|
| `connection_test.py` | Basic robot communication — firmware check, angle reading, calibration |
| `mouvement.py` | Movement library — wave, nod, shake functions with configurable parameters |
| `hand_detection.py` | MediaPipe hand tracking → gesture recognition → robot control (threaded) |
| `face_detection.py` | OpenCV Haar cascade face detection with bounding box overlay |
| `controle_joint.py` | Interactive CLI for individual joint control with safety limits |

## Hardware

- MyCobot 280 M5 (Elephant Robotics)
- USB camera for vision input
- COM3 serial connection at 115200 baud

## Dependencies

```
pymycobot
opencv-python
mediapipe
```

## Next steps

- Tabular Q-learning for autonomous gesture-response mapping
- DQN extension with PyTorch
- Multi-sensor integration (camera + future gripper + force feedback)
