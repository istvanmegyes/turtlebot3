from setuptools import setup
import os
from glob import glob

package_name = 'ros2_course'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Add the following line to include launch files in the package
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros_user',
    maintainer_email='ros_user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello = ros2_course.hello:main', 
	    'talker = ros2_course.talker:main',
	    'listener = ros2_course.listener:main',
            'turtlesim_controller = ros2_course.turtlesim_controller:main',
            'psm_grasp = ros2_course.psm_grasp:main',
            'obstacle_avoidance = ros2_course.obstacle_avoidance:main',
            'move_turtlebot = ros2_course.move_turtlebot:main', 
            'simple_move = ros2_course.simple_move:main',
        ],
    },
)
