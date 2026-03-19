#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math


class MyNode(Node):
    def __init__(self):
        super().__init__("subscriber_node")

        self.create_subscription(
            Float64,
            'topic_1',
            self.sub_cbck,
            10
        )

        self.get_logger().info("Subscriber activo")

    def sub_cbck(self, msg):
        rad = msg.data * 2 * math.pi
        self.get_logger().info(f"Original: {msg.data:.3f} → rad/s: {rad:.3f}")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()