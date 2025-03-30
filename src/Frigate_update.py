from codrone_edu.drone import *

drone = Drone()
drone.pair()
drone.takeoff()
what_color = input("What color B,R,or G")
if what_color == "B":
    drone.set_drone_LED(0,0,225,100)
elif what_color == "R":
    drone.set_drone_LED(225,0,0,100)
else :
    drone.set_drone_LED(0, 225, 0, 100)  # Blue
# drone.load_color_data("color_data")
# drone.set_trim(5, 35)
# for i in range(70):
#     color_d = drone.get_color_data()
#     color = drone.predict_colors(color_d)
# print(color)
#
# if color == ["red", "red"]:
#      drone.set_drone_LED(270, 0, 0, 100)  # Red
#      drone.set_controller_LED(270, 0, 0, 100)  # Red
# elif color == ["green", "green"]:
#      drone.set_drone_LED(0, 270, 0, 100)  # Green
#      drone.set_controller_LED(0, 270, 0, 100)  # Green
# elif color == ["blue", "blue"]:
#      drone.set_drone_LED(0, 0, 270, 100)  # Blue
#      drone.set_controller_LED(0, 0, 270, 100)  # Blue
#Moves up before going through the 2 arches
drone.set_throttle(100)
drone.set_pitch(0)
drone.move(2)
#Goes through the two arches
drone.set_throttle(0)
drone.set_pitch(70)
drone.move(3)
drone.set_pitch(-70)
drone.move(3)
#Goes over the blue arch
for i in range(2):
    drone.set_pitch(50)
    drone.set_throttle(0)
    drone.move(1.5)
    print("AJFKJAFKJFDAJFA")
    drone.set_pitch(0)
    drone.set_throttle(80)
    drone.move(2)
    drone.set_pitch(50)
    drone.set_throttle(0)
    drone.move(1.5)
    drone.set_pitch(0)
    drone.set_throttle(-80)
    drone.move(2)
    drone.set_pitch(-50)
    drone.set_throttle(0)
    drone.move(1.5)
    drone.set_pitch(0)
    drone.set_throttle(80)
    drone.move(2)
    drone.set_pitch(-50)
    drone.set_throttle(0)
    drone.move(1.5)
    drone.set_pitch(0)
    drone.set_throttle(-80)
    drone.move(2)
    
#Goes under the blue drone.move(2)
height = drone.get_height()
goal_height = 60
print(height)
while goal_height + 5 < height or height < goal_height - 5:
    print("Getting To Height")
    while height > goal_height+5:
        drone.set_throttle(-20)
        drone.move(0.01)
        height = drone.get_height()

    while height < goal_height-5:
        drone.set_throttle(20)
        drone.move(0.01)
        height = drone.get_height()
        print(height)
    while goal_height + 5 > height > goal_height - 5:
        break
drone.set_pitch(50)
drone.set_throttle(0)
drone.move(3)

drone.land()
