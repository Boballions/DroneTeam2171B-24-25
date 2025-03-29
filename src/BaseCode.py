from math import sqrt
from time import sleep, monotonic
from simple_pid import PID
from codrone_edu.drone import *


class BRBDrone(Drone):

    def height_correction(self, goal_height):
        """
        Adjusts the drone to a specific target height.

        This function makes the drone ascend or descend until it reaches
        within 5 units of the specified goal height. It continuously
        checks the current height and applies appropriate throttle
        adjustments.

        Args:
            goal_height: The target height for the drone in cm
        """
        self.takeoff()
        height = self.get_height()
        print(height)
        while goal_height + 5 < height or height < goal_height - 5:
            print("Getting To Height")
            while height > goal_height + 5:
                self.set_throttle(-10)
                self.move(0.01)
                height = self.get_height()

            while height < goal_height - 5:
                self.set_throttle(10)
                self.move(0.01)
                height = self.get_height()
                print(height)
            while goal_height + 5 > height > goal_height - 5:
                break
            # self.check_for_hover()

    def simple_move(self, x_speed, y_speed, z_speed, yaw_speed, time):
        """
        Moves the drone with specified speeds for all control axes.

        Sets pitch, roll, throttle, and yaw simultaneously and executes
        the movement for a specified duration. Prints the drone's position
        after movement.

        Args:
            x_speed: Forward/backward speed (-100 to 100)
            y_speed: Left/right speed (-100 to 100)
            z_speed: Up/down speed (-100 to 100)
            yaw_speed: Rotation speed (-100 to 100)
            time: Duration of movement in seconds
        """
        self.set_throttle(z_speed)
        self.set_pitch(x_speed)
        self.set_roll(y_speed)
        self.set_yaw(yaw_speed)
        self.move(time)
        print("My current position is:" + str(self.get_position_data()))

    def battery_check_takeoff(self):
        """
        Performs a battery check before takeoff for safety.

        Checks battery level and decides whether to take off based on
        the percentage. Gives the user a choice if battery is between
        70-80%, and prevents takeoff if below 70%.

        Returns:
            bool: True if takeoff is allowed and executed, False otherwise
        """
        if self.get_battery() > 80:
            self.takeoff()
            print("Good Battery")
            return True
        elif self.get_battery() > 70:
            takeoff_yes_no = input("The battery is at " + str(self.get_battery) + " do you want to takeoff y for yes")
            if takeoff_yes_no == "y":
                return True
            else:
                return False
        else:
            print(
                "Battery Is to low to takeoff ):")
            return False

    def find_color(self):
        """
        Detects colors with the drone's camera and sets LED color.

        Reads the hue value from the color sensor and sets the drone's
        LED color to match what it detects (red, green, or blue).
        Uses specific hue ranges to identify each color.
        """
        hue_raw = self.get_color_data()[1]  # Senses color and checks what it is
        sleep(.1)
        if 0 <= hue_raw < 60:
            self.set_self_LED(255, 0, 0, 100)
            print("RED")
        if 60 <= hue_raw < 180:
            self.set_self_LED(0, 255, 0, 100)
            print("GREEN")
        if 180 <= hue_raw:
            self.set_self_LED(0, 0, 255, 100)
            print("BLUE")

    def check_for_hover(self):
        """
        Waits until the drone enters a stable hovering state.

        Continuously checks the drone's movement state and only
        proceeds when the drone reports it is hovering. This ensures
        stability before the next maneuver.
        """
        while self.get_movement_state() != "Hover":
            sleep(0.1)

    def PID_Setup(self):
        """
        Initializes PID controllers for precision movement.

        Sets up three separate PID controllers for throttle (altitude),
        roll (left/right), and pitch (forward/backward) movements.
        Each controller is configured with appropriate tuning parameters
        and limits for stable flight.
        """
        t = 0
        yfinal = 1.98

        self.pidThrottle = PID(100, 1.5, 0.1, setpoint=1, output_limits=(-100, 100))  # throttle (up and down) pid
        self.pidThrottle.time_fn = monotonic
        self.pidThrottle.sample_time = 0.01

        self.pidRoll = PID(80, .1, 0.03, setpoint=1, output_limits=(-100, 100))  # roll (left and right) pid
        self.pidRoll.time_fn = monotonic
        self.pidRoll.sample_time = 0.01

        self.pidPitch = PID(80, .1, 0.03, setpoint=1, output_limits=(-100, 100))  # pitch (forward and back) pid
        self.pidPitch.time_fn = monotonic
        self.pidPitch.sample_time = 0.01

    def PID_Move(self, x, y, z, timeout=4.5, tolerance=.15):
        """
        Moves the drone to specific 3D coordinates using PID control.

        Uses the PID controllers to precisely navigate to target coordinates.
        Calculates distance to target and adjusts control values continuously
        until position is reached or timeout occurs. Fine-tunes PID parameters
        as the drone approaches target for better accuracy.

        Args:
            x: Target X position in feet (converted to meters internally)
            y: Target Y position in feet (converted to meters internally)
            z: Target Z position in feet (converted to meters internally)
            timeout: Maximum time allowed for positioning in seconds
            tolerance: Acceptable distance error in meters

        The function converts feet to meters by multiplying by 0.3048.
        """
        centering = True
        start_time = self.get_position_data()[0]
        self.pidPitch.setpoint = x
        self.pidPitch.tunings = (80, .1, 0.03)
        self.pidRoll.setpoint = y
        self.pidRoll.tunings = (80, .1, 0.03)
        self.pidThrottle.setpoint = z
        self.pidThrottle.tunings = (80, 1.5, 0.1)
        x *= 0.3048
        y *= 0.3048
        z *= 0.3048

        while centering:  # Loops until it's in position
            current = round(self.get_pos_x(unit="m"), 3), self.get_pos_y(unit="m"), round(self.get_pos_z(unit="m"),
                                                                                          3)  # gets rounded List of x, y, z positions
            dist_to_target = sqrt((current[0] - x) ** 2 + (current[1] - y) ** 2 + (
                        current[2] - z) ** 2)  # Calculates 3d distance to target position
            if dist_to_target <= .25:
                self.pidPitch.tunings = (100, .01, 0)
                self.pidRoll.tunings = (100, .01, 0)
                self.pidThrottle.tunings = (120, .01, .01)  # NEEDS FIXED
            if dist_to_target <= tolerance:  # Checks if self is in correct position
                centering = False
                print(f"--- In position {x}, {y}, {z} ---")
                break
            elif self.get_position_data()[0] - start_time >= timeout:  # timeout for if self can't center
                centering = False
                print(f"--- Centering timeout ---")
                break

            pitch = self.pidPitch(current[0])  # Please note pitch is x and roll is y
            roll = -self.pidRoll(current[1])  # Roll is backwards in the library
            throttle = self.pidThrottle(current[2])

            self.set_pitch(pitch)
            self.set_roll(roll)
            self.set_throttle(throttle)
            self.move(.1)  # CHANGE TIME?

            # print(round(current[0]-x,3), round(pitch,3))
            print(round(current[0] - x, 2), round(current[1] - y, 2), round((z - current[2]), 2),
                  round(roll, 3))  # Printing and graphing
            sleep(.01)
