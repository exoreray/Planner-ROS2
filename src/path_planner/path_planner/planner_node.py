import rclpy
from rclpy.node import Node

from race_msgs.msg import VehicleControlCommand
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
from race_msgs.msg import RppTrajectory
from race_msgs.msg import VehicleState
from race_msgs.msg import TrackedObjects

class PlannerNode(Node):
    def __init__(self):
        super().__init__('planner_node')

        self.subscription_vehicle_state = self.create_subscription(
            VehicleState, '/vehicle/state', self.vehicle_state_callback, 10)
        
        self.subscription_trajectory_command = self.create_subscription(
            RppTrajectory, '/rpc/trajectory_command', self.trajectory_command_callback, 10)
        
        self.subscription_tracked_objects = self.create_subscription(
            TrackedObjects, '/tracked_objects', self.tracked_objects_callback, 10)

        self.publisher_vehicle_control_command = self.create_publisher(
            VehicleControlCommand, '/vehicle/control_command', 10)
        
        self.publisher_path = self.create_publisher(Path, '/planner/path', 10)

    def vehicle_state_callback(self, msg):
        # Process vehicle state
        pass

    def trajectory_command_callback(self, msg):
        # Process trajectory command
        pass

    def tracked_objects_callback(self, msg):
        # Process tracked objects
        pass

    def process_planning(self):
        # Implement your planning algorithm here and publish the output
        
        # Publish VehicleControlCommand
        vehicle_control_command = VehicleControlCommand()
        vehicle_control_command.speed_cmd = 0.0
        vehicle_control_command.steering_cmd = 0.0
        vehicle_control_command.lon_control_type = 1
        self.publisher_vehicle_control_command.publish(vehicle_control_command)
        
        # Publish Path
        path = Path()
        # Add poses to the path.poses list
        self.publisher_path.publish(path)

def main(args=None):
    rclpy.init(args=args)

    planner_node = PlannerNode()

    rclpy.spin(planner_node)

    planner_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
