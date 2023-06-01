import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time

class SimpleMoveNode(Node):
    def __init__(self):
        super().__init__('simple_move')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.msg = Twist()
        self.obstacle_detected = False

    def listener_callback(self, msg):
        range_ahead = msg.ranges[-1]  # We take the forward range (assuming sensor is installed backwards)
        self.get_logger().info('range ahead: "%s"' % range_ahead)
        if range_ahead < 0.6:  # if obstacle closer than 0.5m, stop and turn right
            self.msg.linear.x = 0.0
            self.msg.angular.z = -0.6  # negative value should turn right
            self.obstacle_detected = True
            self.start_time = time.time()  # save the time when we started the turn
        else:
            if self.obstacle_detected and time.time() - self.start_time < 1.57:  # keep turning for ~1.57 seconds
                return
            self.msg.linear.x = 0.1  # move forward at a slow speed
            self.msg.angular.z = 0.0  # stop turning
            self.obstacle_detected = False
        self.publisher_.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)

    simple_move_node = SimpleMoveNode()

    rclpy.spin(simple_move_node)

    simple_move_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

