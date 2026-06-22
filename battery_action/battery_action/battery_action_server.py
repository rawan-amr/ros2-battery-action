import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from battery_action_interfaces.action import ChargeBattery

class BatteryActionServer(Node):

    def __init__(self):
        super().__init__("battery_action_server")

        self._action_server = ActionServer(
            self,
            ChargeBattery,
            "charge_battery",
            self.execute_callback
        )

        self.get_logger().info("Battery Action Server Started")

    def execute_callback(self, goal_handle):
        target_level = goal_handle.request.target_level

        self.get_logger().info(
            f'Received charging request to {target_level}%'
        )

        feedback_msg = ChargeBattery.Feedback()

        current_level = 0

        while current_level < target_level:
            current_level += 10
            
            feedback_msg.current_level = current_level

            goal_handle.publish_feedback(feedback_msg)

            self.get_logger().info(
                f'Charging... {current_level}%'
            )

            time.sleep(1)

        goal_handle.succeed()

        result = ChargeBattery.Result()
        result.success = True

        return result
        

def main(args=None):
    rclpy.init(args=args)

    node = BatteryActionServer()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()