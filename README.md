# LyPolarisLab

Personal research lab — cognitive robotics, reinforcement learning, and AI evaluation.

---

## Current projects

### Cognitive Robotics — MyCobot 280 M5

Building an autonomous robotic arm that learns from human interaction.

- **Gesture-based control**: MediaPipe hand tracking → real-time robot response (wave, nod, shake)
- **Face detection**: OpenCV Haar cascades for human presence awareness
- **Joint control**: Interactive joint manipulation interface
- **Movement library**: Reusable motion functions with configurable speed and repetitions

Currently implementing tabular Q-learning for autonomous behavior. Next step: extending to DQN with PyTorch.

→ `robotics/mycobot280/`

### COGNI-TEST *(in progress)*

Evaluation protocol for LLM cognitive capabilities — testing contradiction detection, expressed uncertainty, and response revision under controlled conditions.

- 2×2 experimental design (prompt length × contradiction presence)
- 3 evaluation conditions (initial response, neutral re-examination, guided correction)
- Metrics: F1, precision, recall, confusion matrices
- Python + LLM API + Pandas + scikit-learn

→ Coming soon

### Black Hole Simulator

Schwarzschild radius calculator using real NASA data. Two versions:

- **v1**: Basic calculator with matplotlib log-scale visualization (stellar vs supermassive)
- **v2**: Interactive CLI with dictionaries of black holes (stellar, intermediate, supermassive) and astronomical objects — simulation, exploration, comparison, and custom object creation

→ `astronomy/`

---

## Stack

Python · pymycobot · OpenCV · MediaPipe · Matplotlib · Pandas · scikit-learn · PyTorch *(learning)*

---

## About

I'm an early-career AI researcher exploring how autonomous systems can develop adaptive behavior through interaction. My work sits at the intersection of robotics, reinforcement learning, and cognitive science — with a particular interest in how machines handle uncertainty and self-evaluate.

Currently: M2 Data & AI at INSEEC Paris | BI Developer at Framatome (apprenticeship)
