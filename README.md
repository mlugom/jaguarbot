# Jaguarbot's operation and simulation ROS package

This is a ROS package used to operate and simulate the rover for data acquisition on mango's anthracnose **Jaguarbot**, which is a prototype of a mobile robot designed and manufactured for academic purposes, as part of a Degree's Project.

**Author:** Manuel Esteban Lugo Madrid. Degree's Project 2022-2 developed with Eng. Flavio Augusto Prieto Ortiz from the National University of Colombia.

## How to use this package:

This package can be used with two purposes: first one is **to operate the robot**, and second one is **to run a simulation with a naive robot model to check functionality**.

### Requirements
1. Ubuntu 20.XX, recommended Ubuntu 20.04 LTS
2. ROS installed on your machine (ROS Noetic is highly recommended to keep robustness in functionality)
3. Rosbridge Server ROS package installed

**Aditional Requirements:**
1. For simulation:
   1. Gazebo app and gazebo-ros package installed

2. For physical operation:
   1. Jaguarbot (or any other robot prototype which can be operated through a differential drive)
   2. Raspberry PI with Ubuntu 20.04 LTS system and ROS Noetic installed.
   3. Wifi connection, to grant communication between the robot and the control computer.

### Preparation
There is no preparation required in simulation mode. However, it is needed some preparation to run the physical operation, which consists in the following:

* Connect Raspberry Pi to local network. It can be done by following this [tutorial](https://youtu.be/sO1pw93GGkU)
* Check the IP address of your local machine.
  ~~~~
  hostname -I
  ~~~~

* Change your RPi variable ROS_MASTER_URI, by running the following command line (on the RPi terminal):

  ~~~~
  export ROS_MASTER_URI=http://LOCAL_MACHINE_IP_ADDRESS:11311
  ~~~~
  replacing LOCAL_MACHINE_IP_ADDRESS with your actual local machine IP address.


And that's it! By now, you should be ready to use the package to command the robot.

### Hands on

#### For simulation
Once you have installed and sourced this package, follow the next steps:
1. Launch a terminal and run the following command
   ~~~~
   roscore
   ~~~~
2. Launch another terminal and run the following command line to launch the nodes corresponding to the simulation
   ~~~~
   roslaunch jaguarbot simulation.launch
   ~~~~
   You should now see the robot model spawned on Gazebo.
3. Run the simulation by clicking the "Play" button on Gazebo.
4. Go to web/index.html and open it on a web browser.
5. That's it. You can now command the simulated robot by clicking the instructions available in the GUI.


#### For physical operation
Once you have installed and sourced this package **both** on your machine and your RPi, and prepared properly as explained above, follow the next steps:
1. Launch a terminal and run the following command
   ~~~~
   roscore
   ~~~~
2. Launch another terminal and run the following command line to launch the nodes corresponding to the message bypassing:
   ~~~~
   roslaunch jaguarbot host.launch
   ~~~~
3. Grant permissions to use the GPIO port of your RPi by running (on your RPi) the following command:
   ~~~~
   sudo chmod 777 /dev/gpiomem
   ~~~~
4. Check your RPi ROS_MASTER_URI value by running:
   ~~~~
   echo $ROS_MASTER_URI
   ~~~~
   You should get the address explained above. If you don't, please check again the *Preparation* section.
5. Launch (on your RPi) the following command:
   ~~~~
   roslaunch jaguarbot jaguarbot.launch
   ~~~~
6. On your machine, go to web/index.html and open it on a web browser.
7. That's it. You can now command the physical robot by clicking the instructions available in the GUI.


## Videos:

[Functionality video](https://youtu.be/qUHUN6ycA-Q)
