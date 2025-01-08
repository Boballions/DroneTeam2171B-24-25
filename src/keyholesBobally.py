from codrone_edu.drone import *
drone = Drone()
drone.pair()

# drone.load_color_data("color_data")
height_for_yellow = 90

# for i in range(100):
#
#     color_data = drone.get_color_data()
#
#     color = drone.predict_colors(color_data)
#
# print(color)
#
#
#
# if color == ["red", "red"]:
#     drone.set_drone_LED(255, 0, 0, 100)  # Red
#     drone.set_controller_LED(255, 0, 0, 100)  # Red
# elif color == ["green", "green"]:
#     drone.set_drone_LED(0, 255, 0, 100)  # Green
#     drone.set_controller_LED(0, 255, 0, 100)  # Green
# elif color == ["blue", "blue"]:
#     drone.set_drone_LED(0, 0, 255, 100)  # Blue
#     drone.set_controller_LED(0, 0, 255, 100)  # Blue
#
#
#
# drone.calibrate()
drone.takeoff()
height = drone.get_height()
print(height)

while height_for_yellow + 3 < height or height < height_for_yellow - 3:
    print("Loop Runing")
    while height > height_for_yellow:
        drone.set_throttle(-15)
        drone.move(0.01)
        height = drone.get_height()

    while height < height_for_yellow:
        drone.set_throttle(15)
        drone.move(0.01)
        height = drone.get_height()
    if height_for_yellow + 3 < height > height_for_yellow - 3:
        break

print("Correct height, moving forward!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
drone.set_throttle(50)
drone.move(1.64)
print("I'm Up")
drone.set_throttle(0)
drone.set_pitch(50)
drone.move(2.5)
print("I'm Forward")
drone.set_pitch(0)
drone.set_throttle(-50)
drone.move(0.8)
print("I'm Down")
drone.set_throttle(0)
drone.set_pitch(0)
drone.set_roll(50)
drone.move(3)
print("I'm Right")
drone.set_pitch(-10)
drone.move(1)
print("I'm landing")
drone.spiral(50, 5, 1)
drone.land()