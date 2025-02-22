from codrone_edu.drone import *

drone = Drone()
drone.pair()
drone.takeoff()
# drone.load_color_data("color_data")
# drone.set_trim(5, 35)
# for i in range(70):
#     color_d = drone.get_color_data()
#     color = drone.predict_colors(color_d)
# print(color)
#
# if color == ["red", "red"]:
#      drone.set_drone_LED(255, 0, 0, 100)  # Red
#      drone.set_controller_LED(255, 0, 0, 100)  # Red
# elif color == ["green", "green"]:
#      drone.set_drone_LED(0, 255, 0, 100)  # Green
#      drone.set_controller_LED(0, 255, 0, 100)  # Green
# elif color == ["blue", "blue"]:
#      drone.set_drone_LED(0, 0, 255, 100)  # Blue
#      drone.set_controller_LED(0, 0, 255, 100)  # Blue
#Moves up before going through the 2 arches
drone.set_throttle(100)
drone.set_pitch(0)
drone.move(0.5)
#Goes through the two arches
drone.set_throttle(0)
drone.set_pitch(55)
drone.move(3)
drone.set_pitch(-55)
drone.move(1.6)
#Goes over the blue arch
drone.set_pitch(0)
drone.set_throttle(55)
drone.move(2)
drone.set_pitch(50)
drone.set_throttle(0)
drone.move(1.2)
#Goes under the blue arch
drone.set_throttle(-100)
drone.set_pitch(0)
drone.move(1.2)
#Goes under the blue, over to the red
drone.set_pitch(-60)
drone.set_throttle(0)
drone.move(1.75)
drone.set_throttle(100)
drone.set_pitch(0)
drone.move(1)
#Completes the red
drone.set_throttle(0)
drone.set_pitch(-50)
drone.move(1.4)
drone.set_pitch(0)
drone.set_throttle(-100)
drone.move(1)
drone.set_throttle(0)
drone.set_pitch(31)
drone.move(2)
#Starts the second figure 8
drone.set_pitch(0)
drone.set_throttle(55)
drone.move(2)
drone.set_pitch(50)
drone.set_throttle(0)
drone.move(1.2)
#Goes under the blue arch
drone.set_throttle(-100)
drone.set_pitch(0)
drone.move(1.2)
#Goes under the blue, over to the red
drone.set_pitch(-60)
drone.set_throttle(0)
drone.move(1.7)
drone.set_throttle(100)
drone.set_pitch(0)
drone.move(1)
#Completes the red
drone.set_throttle(0)
drone.set_pitch(-50)
drone.move(1.35)
drone.set_pitch(0)
drone.set_throttle(-100)
drone.move(1.2)
drone.set_throttle(0)
drone.set_pitch(100)
drone.move(2)
drone.land()
