#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random


class MyNode(Node):
    def __init__(self):
        super().__init__("publisher_node")

        self.publisher_ = self.create_publisher(
            Float64,
            'topic_1',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.cbck
        )

        self.get_logger().info("Publisher activo")

    def cbck(self):
        msg = Float64()
        msg.data = random.uniform(0.0, 1.0)
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()