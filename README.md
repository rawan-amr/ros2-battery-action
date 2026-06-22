# ROS2 Battery Action

A ROS2 project that demonstrates how to create and use custom Actions by implementing a battery charging simulation using ROS2 Jazzy and Python.

## Overview

This project simulates a battery charging process using a custom ROS2 Action.

The client sends a target battery level as a goal, while the server processes the request, continuously publishes charging progress as feedback, and finally returns a result when charging is completed.

## System Architecture

```text
Action Client
      |
      | Goal (target_level)
      v
Action Server
      |
      | Feedback (current_level)
      v
Action Client

      |
      | Result (success)
      v
Action Client
```

## Project Structure

```text
ros2-battery-action
├── battery_action
│   ├── battery_action_server.py
│   └── battery_action_client.py
│
├── battery_action_interfaces
│   └── action
│       └── ChargeBattery.action
│
└── .gitignore
```

## Custom Action Definition

```text
# Goal
int64 target_level

---

# Result
bool success

---

# Feedback
int64 current_level
```

## Features

- Custom ROS2 Action interface
- Action Server implementation
- Action Client implementation
- Goal handling
- Feedback publishing
- Result reporting
- Simulated battery charging process

## Technologies Used

- ROS2 Jazzy
- Python
- rclpy
- ROS2 Actions

## Build

```bash
colcon build

source install/setup.bash
```

## Run Action Server

```bash
ros2 run battery_action battery_action_server
```

## Run Action Client

```bash
ros2 run battery_action battery_action_client
```

## Example Output

### Server

```text
Received charging request to 80%
Charging... 10%
Charging... 20%
Charging... 30%
Charging... 40%
Charging... 50%
Charging... 60%
Charging... 70%
Charging... 80%
```

### Client

```text
Goal accepted
Current Level: 10%
Current Level: 20%
Current Level: 30%
Current Level: 40%
Current Level: 50%
Current Level: 60%
Current Level: 70%
Current Level: 80%
Charging Completed: True
```

## Learning Outcomes

Through this project I learned:

- Creating custom ROS2 Action interfaces
- Implementing Action Servers
- Implementing Action Clients
- Goal, Feedback, and Result communication
- ROS2 package organization
- Building and running ROS2 projects
