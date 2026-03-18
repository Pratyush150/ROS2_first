# ROS2 Turtle Controller Package

This package contains a set of ROS2 nodes built for learning and experimenting with **robot motion, communication, and control using turtlesim**.

It demonstrates core ROS2 concepts such as:

* Nodes
* Publishers & Subscribers
* Topics (`/cmd_vel`, `/turtle1/pose`)
* Timers and callbacks
* Motion control logic

---

## 📦 Package Structure

```
my_robot_controller/
├── __init__.py
├── draw_circle.py
├── my_first_node.py
├── pose_subscriber.py
├── turtle_controller.py
```

---

## 🚀 Nodes Overview

### 1. `my_first_node.py`

* Basic ROS2 node
* Used to understand node initialization and logging

👉 Purpose: **Foundation of ROS2 nodes**

---

### 2. `draw_circle.py`

* Publishes velocity commands (`Twist`) to `/cmd_vel`
* Makes the turtle move in a circular path

👉 Key Concepts:

* Publisher
* `geometry_msgs/Twist`
* Continuous motion

---

### 3. `pose_subscriber.py`

* Subscribes to `/turtle1/pose`
* Reads position and orientation of the turtle

👉 Key Concepts:

* Subscriber
* Real-time data from topics

---

### 4. `turtle_controller.py`

* Combines subscriber + publisher
* Uses turtle position to control movement
* Implements basic wall detection and turning behavior

👉 Key Concepts:

* Feedback-based control
* Decision logic using sensor data
* Reactive robotics behavior

---

## 🧠 Core Concepts Demonstrated

### 🔹 Topics

* `/cmd_vel` → velocity commands
* `/turtle1/pose` → turtle position data

### 🔹 Message Types

* `Twist` → velocity control
* `Pose` → position and orientation

### 🔹 Architecture

```
Pose Subscriber → Decision Logic → Velocity Publisher → Turtle Movement
```

---

## ⚙️ How to Run

### 1. Start turtlesim

```bash
ros2 run turtlesim turtlesim_node
```

---

### 2. Run a node

#### Draw Circle

```bash
ros2 run my_robot_controller draw_circle
```

#### Pose Subscriber

```bash
ros2 run my_robot_controller pose_subscriber
```

#### Turtle Controller

```bash
ros2 run my_robot_controller turtle_controller
```

---

## 🎯 What This Project Teaches

* How ROS2 nodes communicate via topics
* Difference between publishers and subscribers
* How to control a robot using velocity commands
* How to use feedback (pose) to influence motion
* Event-driven programming with callbacks

---

## 🚧 Limitations

* No advanced control algorithms (PID, SLAM, etc.)
* Works only in turtlesim (not real robot yet)
* Hardcoded thresholds for wall detection

---

## 🔜 Future Improvements

* Implement PID control for smoother motion
* Add obstacle avoidance logic
* Integrate with real robot (TurtleBot)
* Extend to ROS2 Navigation (Nav2)
* Add simulation with Gazebo

---

## 🧭 Learning Outcome

This package is part of a hands-on journey to move from:

```
Writing code → Understanding ROS systems → Building autonomous robots
```

---

## 👤 Author

Pratyush150
