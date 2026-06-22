import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from battery_action_interfaces.action import ChargeBattery


class BatteryActionClient(Node):

    def __init__(self):
        super().__init__('battery_action_client')

        self._action_client = ActionClient(
            self,
            ChargeBattery,
            'charge_battery'
        )

    def send_goal(self, target_level):

        goal_msg = ChargeBattery.Goal()
        goal_msg.target_level = target_level

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        self._send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(
            self.get_result_callback
        )

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f'Current Level: {feedback.current_level}%'
        )

    def get_result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            f'Charging Completed: {result.success}'
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    action_client = BatteryActionClient()

    target_level = 80
    
    action_client.send_goal(target_level)

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()