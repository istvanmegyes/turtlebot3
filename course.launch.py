from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_prefix

def generate_launch_description():
    turtlebot3_gazebo_prefix = get_package_prefix('turtlebot3_gazebo')
    turtlebot3_cartographer_prefix = get_package_prefix('turtlebot3_cartographer')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'launch', turtlebot3_gazebo_prefix + '/share/turtlebot3_gazebo/launch/turtlebot3_world.launch.py'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['ros2', 'launch', turtlebot3_cartographer_prefix + '/share/turtlebot3_cartographer/launch/cartographer.launch.py', 'use_sim_time:=True'],
            output='screen'
        ),
        Node(
            package='ros2_course',
            namespace='robot',
            executable='simple_move',
            output='screen'
        )
    ])

