# Custom PX4 Firmware - Modifications by Davi Juvêncio Gomes de Sousa

This repository is a modification of the [PX4 Autopilot](https://github.com/PX4/PX4-Autopilot) repository. It has been customized for the implementation of the **Hierarchical Vision-Based Formation Control**, which is the result of my doctoral thesis titled **"Formação Espaço-Temporal de Veículos Aéreos não Tripulados"** (Space-Time Formation of Unmanned Aerial Vehicles).

## Modifications by Davi Juvêncio Gomes de Sousa

The modifications in this repository were made by **Davi Juvêncio Gomes de Sousa**. For more information or to get in touch, you can reach me through the following channels:

- 📧 [Email](mailto:davijuvencio@gmail.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/davijuvencio/)
- 📄 [Currículo Lattes](http://lattes.cnpq.br/4271565381722032)

![LinkedIn Badge](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white) ![Gmail Badge](https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white)

---

## Objective

This simulator was created to test the **Hierarchical Vision-Based Formation Control** algorithm, a key aspect of my doctoral research. The goal of the algorithm is to enable multiple UAVs (Unmanned Aerial Vehicles) to maintain coordinated formation using vision-based techniques. The research focuses on the space-time formation of UAVs and how they can operate autonomously in complex environments.

---

## Installation

### Dependencies Installation

Run the following commands to install the necessary dependencies:

```bash
sudo apt install ninja-build exiftool ninja-build protobuf-compiler libeigen3-dev genromfs xmlstarlet libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev python3-pip gawk
pip3 install packaging numpy empy toml pyyaml jinja2 pyargparse kconfiglib jsonschema future pandas jinja2 pyserial cerberus pyulog==0.7.0 toml pyquaternion empy
sudo apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

### ROS Installation

Follow the official ROS Noetic installation guide:  
[ROS: Getting Started](https://wiki.ros.org/noetic/Installation/Ubuntu)

### Gazebo Installation

Remove any existing Gazebo installation and install the latest version:

```bash
sudo apt-get remove gazebo* 
sudo apt-get remove libgazebo*
sudo apt-get remove ros-noetic-gazebo*
curl -sSL http://get.gazebosim.org | sh
```

### Additional Dependencies for Gazebo and ROS

Install additional ROS and Gazebo-related dependencies:

```bash
sudo apt-get install ros-noetic-moveit-msgs -y
sudo apt-get install ros-noetic-object-recognition-msgs -y
sudo apt-get install ros-noetic-octomap-msgs -y
sudo apt-get install ros-noetic-camera-info-manager -y
sudo apt-get install ros-noetic-control-toolbox -y
sudo apt-get install ros-noetic-polled-camera -y
sudo apt-get install ros-noetic-effort-controllers -y
sudo apt-get install ros-noetic-joint-state-controller -y
sudo apt-get install ros-noetic-position-controllers -y
sudo apt-get install ros-noetic-velocity-controllers -y
sudo apt-get install ros-noetic-mavros -y
sudo apt-get install build-essential python3-rosdep python3-catkin-tools -y
sudo apt-get install libusb-dev python3-osrf-pycommon libspnav-dev libbluetooth-dev libcwiid-dev libgoogle-glog-dev -y
pip3 install py3rosmsgs catkin_pkg rospkg
```

Clone the repository:

```bash
https://github.com/davijuvencio/PX4-Vision-Based-Formation-Control-Simulator.git
```

### MAVROS Installation

Install MAVROS and configure geographic datasets:

```bash
sudo apt install ros-noetic-mavros ros-noetic-mavros-extras -y
cd PX4-Vision-Based-Formation-Control-Simulator/files/
sudo chmod a+x ./install_geographiclib_datasets.sh
sudo ./install_geographiclib_datasets.sh
```

---

## Simulator Configuration

1. Build and configure the PX4 SITL environment:

    ```bash
    cd ~/PX4-Vision-Based-Formation-Control-Simulator
    mv platforms/nuttx/NuttX/nuttx/.gitim platforms/nuttx/NuttX/nuttx/.git 
    mv platforms/nuttx/NuttX/apps/.gitim platforms/nuttx/NuttX/apps/.git 
    mv Tools/sitl_gazebo/external/OpticalFlow/external/klt_feature_tracker/.gitim Tools/sitl_gazebo/external/OpticalFlow/external/klt_feature_tracker/.git 
    mv Tools/sitl_gazebo/external/OpticalFlow/.gitim Tools/sitl_gazebo/external/OpticalFlow/.git 
    mv Tools/sitl_gazebo/.gitim Tools/sitl_gazebo/.git 
    mv Tools/simulation-ignition/.gitim Tools/simulation-ignition/.git 
    mv Tools/jMAVSim/jMAVlib/.gitim Tools/jMAVSim/jMAVlib/.git 
    mv Tools/jMAVSim/.gitim Tools/jMAVSim/.git 
    mv Tools/flightgear_bridge/models/TF-R1/.gitim Tools/flightgear_bridge/models/TF-R1/.git 
    mv Tools/flightgear_bridge/models/TF-G2/.gitim Tools/flightgear_bridge/models/TF-G2/.git 
    mv Tools/flightgear_bridge/models/TF-G1/.gitim Tools/flightgear_bridge/models/TF-G1/.git 
    mv Tools/flightgear_bridge/models/Rascal/.gitim Tools/flightgear_bridge/models/Rascal/.git 
    mv Tools/flightgear_bridge/.gitim Tools/flightgear_bridge/.git 
    mv Tools/jsbsim_bridge/models/ATI-Resolution/.gitim Tools/jsbsim_bridge/models/ATI-Resolution/.git 
    mv Tools/jsbsim_bridge/models/Rascal/.gitim Tools/jsbsim_bridge/models/Rascal/.git 
    mv Tools/jsbsim_bridge/.gitim Tools/jsbsim_bridge/.git 
    mv src/modules/micrortps_bridge/micro-CDR/.gitim src/modules/micrortps_bridge/micro-CDR/.git 
    mv src/modules/mavlink/mavlink/.gitim src/modules/mavlink/mavlink/.git 
    mv src/modules/mavlink/mavlink/pymavlink/.gitim src/modules/mavlink/mavlink/pymavlink/.git 
    mv src/modules/microdds_client/Micro-XRCE-DDS-Client/.gitim src/modules/microdds_client/Micro-XRCE-DDS-Client/.git 
    mv src/lib/events/libevents/.gitim src/lib/events/libevents/.git 
    mv src/lib/events/libevents/libs/cpp/parse/nlohmann_json/.gitim src/lib/events/libevents/libs/cpp/parse/nlohmann_json/.git 
    mv src/lib/crypto/libtommath/.gitim src/lib/crypto/libtommath/.git 
    mv src/lib/crypto/monocypher/.gitim src/lib/crypto/monocypher/.git 
    mv src/lib/crypto/libtomcrypt/.gitim src/lib/crypto/libtomcrypt/.git 
    mv src/drivers/gps/devices/.gitim src/drivers/gps/devices/.git 
    mv src/drivers/uavcan/libuavcan/dsdl/.gitim src/drivers/uavcan/libuavcan/dsdl/.git 
    mv src/drivers/uavcan/libuavcan/.gitim src/drivers/uavcan/libuavcan/.git 
    mv src/drivers/uavcan/libuavcan/libuavcan/dsdl_compiler/pyuavcan/.gitim src/drivers/uavcan/libuavcan/libuavcan/dsdl_compiler/pyuavcan/.git 
    mv src/drivers/uavcan_v1/legacy_data_types/.gitim src/drivers/uavcan_v1/legacy_data_types/.git 
    mv src/drivers/uavcan_v1/libcanard/.gitim src/drivers/uavcan_v1/libcanard/.git 
    mv src/drivers/uavcan_v1/public_regulated_data_types/.gitim src/drivers/uavcan_v1/public_regulated_data_types/.git 
    DONT_RUN=1 make px4_sitl_default gazebo
    ```

2. Set up the ROS workspace:

    ```bash
    cd ~
    mkdir -p ~/catkin_ws/src
    mkdir -p ~/catkin_ws/scripts
    cd catkin_ws/src && catkin_init_workspace
    cd .. && catkin_make
    ```

3. Add necessary files to the workspace:

    ```bash
    cd ~/catkin_ws/src
    cp -r ~/PX4-Vision-Based-Formation-Control-Simulator/files/gazebo_ros_pkgs .
    cd ~/catkin_ws
    catkin_make
    ```

4. Configure environment variables:

    ```bash
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
    echo "source ~/PX4-Vision-Based-Formation-Control-Simulator/Tools/setup_gazebo.bash ~/PX4-Vision-Based-Formation-Control-Simulator/ ~/PX4-Vision-Based-Formation-Control-Simulator/build/px4_sitl_default" >> ~/.bashrc
    echo "export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:~/PX4-Vision-Based-Formation-Control-Simulator" >> ~/.bashrc
    echo "export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:~/PX4-Vision-Based-Formation-Control-Simulator/Tools/sitl_gazebo" >> ~/.bashrc
    source ~/.bashrc
    ```

5. Launch the simulator:

    ```bash
    cd ~/PX4-Vision-Based-Formation-Control-Simulator
    roslaunch px4 mavros_posix_sitl.launch
    rostopic echo /mavros/state
    ```

6. Set up Gazebo models:

    ```bash
    cd ~
    mkdir .gazebo
    cd ~/.gazebo
    cp -r ~/PX4-Vision-Based-Formation-Control-Simulator/files/gazebo_models . 
    mv gazebo_models models
    cd ~
    ```
    
7. Final configuration:

    ```bash
    cd ~/PX4-Vision-Based-Formation-Control-Simulator
    cp -r files/simulator-files/init.d-posix/* ROMFS/px4fmu_common/init.d-posix/
    cp -r files/simulator-files/launch/* launch/
    cp -r files/simulator-files/worlds/* Tools/sitl_gazebo/worlds/
    cp -r files/simulator-files/models/* Tools/sitl_gazebo/models/
    cd ~/.gazebo/models/
    rm -r stereo_camera/ 3d_lidar/ 3d_gpu_lidar/ hokuyo_lidar/
    cd ~/PX4-Vision-Based-Formation-Control-Simulator
    make px4_sitl_default gazebo
    ```
   
8. Hello World:

    ```bash
    cd ~/PX4-Vision-Based-Formation-Control-Simulator
    roslaunch px4 indoor1.launch
    cd ~/PX4-Vision-Based-Formation-Control-Simulator/src/helloWorld
    python3 multirotor_communication.py iris 0
    python3 multirotor_keyboard_control.py iris 1 vel
    ```
