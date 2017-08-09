# Execution steps

1. Translate the Scratch program to Python

```
roscd scratch2ros/scripts
python scratch2python example.sb2
```
  
2. Launch the robot (simulation)

**ROS specific**:

* Empty world:

```
roslaunch kobuki_gazebo kobuki_empty_world.launch --screen
```

* World with some obstacles:

```
roslaunch turtlebot_gazebo turtlebot_world.launch
```

**ICE specific**:

* Simple world:

```
gazebo kobuki-simple.world 
```

3. Execute the translated python program

```
python node.py
```
