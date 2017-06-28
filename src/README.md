# Execution steps

1. Translate the Scratch program to Python

 ./scratch2python example.sb2
  
2. Launch the kobuki robot in gazebo

 roslaunch kobuki_gazebo kobuki_empty_world.launch --screen

3. Launch the translated program

 roslaunch scratch_kobuki scratch_kobuki.launch
