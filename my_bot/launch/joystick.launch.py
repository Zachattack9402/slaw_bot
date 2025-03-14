from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchDescription('use_sim_time')

    joy_params = os.path.join(get_package_share_directory('articubot_one'),'config','joystick.yaml')

    joy_node = Node(
            package='joy',
            executable='joy_node',
            parameters=[joy_params,{'use_sime_time': use_sim_time}],
         )
    
    teleop_node = Node(
            package='teleop_twist_joy', 
            executable='teleop_node',
            name = 'teleop_node',
            parameters=[joy_params,{'use_sim_time': use_sim_time}],
            remappings=[('/cmd_vel', '/cmd_vel_joy')]
            )

    return LaunchDescription([
        joy_node       
    ])
