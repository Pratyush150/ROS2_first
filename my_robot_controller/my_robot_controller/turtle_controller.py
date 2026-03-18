#!/usr/bin/env python3
import cmd
from functools import partial
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.previous_x = 0.0
        self.cmd_vel_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.get_logger().info("TurtleControllerNode initialized")

    def pose_callback(self, msg: Pose):
       
       cmd = Twist()

       if msg.x > 9.0 or msg.x < 2.0 or msg.y > 9.0 or msg.y < 2.0:
           # Near wall → turn (circle behavior)
           cmd.linear.x = 1.0
           cmd.angular.z = 0.9
       else:
           # Normal movement
           cmd.linear.x = 5.0
           cmd.angular.z = 0.0

       self.cmd_vel_publisher.publish(cmd)

       if msg.x > 5.5 and self.previous_x <= 5.5:
              self.previous_x = msg.x
              # Change pen color to red when x > 5.5
              self.get_logger().info("Changing pen color to red")
              self.call_set_pen_service(r=255, g=0, b=0, width=3, off=0)
       elif msg.x <= 5.5 and self.previous_x > 5.5:
           self.previous_x = msg.x
           # Change pen color to blue when x <= 5.5
           self.get_logger().info("Changing pen color to blue")
           self.call_set_pen_service(r=0, g=0, b=255, width=3, off=0)

    def call_set_pen_service(self, r, g, b, width, off):
        client=self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for /turtle1/set_pen service...")
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self, future):
        try:
            response = future.result()
            self.get_logger().info("SetPen service called successfully")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()