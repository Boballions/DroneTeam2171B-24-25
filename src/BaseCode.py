from time import sleep

from codrone_edu.drone import *


class BRBDrone(Drone):

    def height_correction(self, goal_height):
        self.takeoff()
        height = self.get_height()
        print(height)
        while goal_height + 5 < height or height < goal_height - 5:
            print("Getting To Height")
            while height > goal_height+5:
                self.set_throttle(-10)
                self.move(0.01)
                height = self.get_height()

            while height < goal_height-5:
                self.set_throttle(10)
                self.move(0.01)
                height = self.get_height()
                print(height)
            while goal_height + 5 > height > goal_height - 5:
                break
            # self.check_for_hover()

    def simple_move(self, x_speed, y_speed, z_speed, yaw_speed, time):
        self.set_throttle(z_speed)
        self.set_pitch(x_speed)
        self.set_roll(y_speed)
        self.set_yaw(yaw_speed)
        self.move(time)
        print("My current position is:" + str(self.get_position_data()))

    def battery_check_takeoff(self):
        if self.get_battery()>80:
            self.takeoff()
            print("Good Battery")
            return True
        elif self.get_battery()>70:
            takeoff_yes_no = input("The battery is at " + str(self.get_battery) + " do you want to takeoff y for yes")
            if takeoff_yes_no == "y" :
                return True
            else:
                return False
        else:
            print("Battery Is to low to takeoff ): ):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):")
            return False

    def find_color(self):
        self.load_color_data("color_data")
        color = "not found"
        for i in range(70):
            color_d = self.get_color_data()
            color = self.predict_colors(color_d)
        print(color)

        if color == ["red", "red"]:
            self.set_self_LED(255, 0, 0, 100)  # Red
            self.set_controller_LED(255, 0, 0, 100)  # Red
        elif color == ["green", "green"]:
            self.set_self_LED(0, 255, 0, 100)  # Green
            self.set_controller_LED(0, 255, 0, 100)  # Green
        elif color == ["blue", "blue"]:
            self.set_self_LED(0, 0, 255, 100)  # Blue
            self.set_controller_LED(0, 0, 255, 100)  # Blue
            self.set_controller_LED(0, 0, 255, 100)  # Blue
        # Moves up before going through the 2 arches

    def check_for_hover(self):
        while self.get_movement_state() != "Hover":
            sleep(0.1)

