from codrone_edu.drone import *

drone = Drone()
drone.pair()
drone.takeoff()
height = drone.get_height()
print(height)
height_for_figure = 100
while height_for_figure + 2 < height or height < height_for_figure - 3:
    print("Loop Running")
    while height > height_for_figure:
        drone.set_throttle(-20)
        drone.move(0.01)
        height = drone.get_height()
        print(height)
        '''if height == 999.9:
            height = drone.get_height()
            print(height)'''

    while height < height_for_figure:
        drone.set_throttle(30)
        drone.move(0.01)
        height = drone.get_height()
        print(height)
        '''if height == 999.9:
            height = drone.get_height()
            print(height)'''
    if height_for_figure + 2 > height > height_for_figure - 2:
        print("code workedasdfghjdsgfaBGFDSHEhgSAfdSghfxkjreshtewa")
        break

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
"""drone.set_throttle(100)
drone.set_pitch(0)
drone.move(0.5)"""
height = drone.get_height()
print(height)
#Goes through the two arches
drone.set_throttle(0)
drone.set_pitch(55)
drone.move(3)
drone.set_pitch(-55)
drone.move(1.6)
height = drone.get_height()
print(height)
#Goes over the blue arch
drone.set_pitch(0)
drone.set_throttle(55)
drone.move(1.8)
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
drone.move(1.2)
#Completes the red
drone.set_throttle(0)
drone.set_pitch(-50)
drone.move(1.3)
drone.set_pitch(0)
drone.set_throttle(-100)
drone.move(0.75)
drone.set_throttle(0)
drone.set_pitch(31)
drone.move(1.5)
#Starts the second figure 8
drone.set_pitch(0)
drone.set_throttle(55)
drone.move(2)
drone.set_pitch(50)
drone.set_throttle(0)
drone.move(0.8)
#Goes under the blue arch
drone.set_throttle(-100)
drone.set_pitch(0)
drone.move(1.3)
#Goes under the blue, over to the red
drone.set_pitch(-60)
drone.set_throttle(0)
drone.move(1.6)
drone.set_throttle(100)
drone.set_pitch(0)
drone.move(1)
#Completes the red
drone.set_throttle(0)
drone.set_pitch(-50)
drone.move(1.35)
drone.set_pitch(0)
drone.set_throttle(-100)
drone.move(0.75)
drone.set_throttle(0)
drone.set_pitch(31)
drone.move(2)
drone.land()