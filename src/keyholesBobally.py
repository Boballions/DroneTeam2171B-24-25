from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.load_color_data("color_data")
height_for_yellow = 128
for i in range(70):
    color_data = drone.get_color_data()

    color = drone.predict_colors(color_data)
print(color)

<<<<<<< Updated upstream
for i in range(500):
    color_data = drone.get_color_data()
    color = drone.predict_colors(color_data)
    print(color)

print(color)

if color == ["red", "red"]:
    drone.set_drone_LED(255, 0, 0, 100)  # Red
    drone.set_controller_LED(255, 0, 0, 100)  # Red
elif color == ["green", "green"]:
    drone.set_drone_LED(0, 255, 0, 100)  # Green
    drone.set_controller_LED(0, 255, 0, 100)  # Green
elif color == ["blue", "blue"]:
    drone.set_drone_LED(0, 0, 255, 100)  # Blue
    drone.set_controller_LED(0, 0, 255, 100)  # Blue



#drone.calibrate()
=======
if color == ["red", "red"]:
     drone.set_drone_LED(255, 0, 0, 100)  # Red
     drone.set_controller_LED(255, 0, 0, 100)  # Red
elif color == ["green", "green"]:
     drone.set_drone_LED(0, 255, 0, 100)  # Green
     drone.set_controller_LED(0, 255, 0, 100)  # Green
elif color == ["blue", "blue"]:
     drone.set_drone_LED(0, 0, 255, 100)  # Blue
     drone.set_controller_LED(0, 0, 255, 100)  # Blue


drone.calibrate()
>>>>>>> Stashed changes
drone.takeoff()
height = drone.get_height()
print(height)

while height_for_yellow + 2 < height or height < height_for_yellow - 3:
    print("Loop Running")
    while height > height_for_yellow:
        drone.set_throttle(-20)
        drone.move(0.01)
        height = drone.get_height()
        print(height)
        '''if height == 999.9:
            height = drone.get_height()
            print(height)'''

    while height < height_for_yellow:
        drone.set_throttle(30)
        drone.move(0.01)
        height = drone.get_height()
        print(height)
        '''if height == 999.9:
            height = drone.get_height()
            print(height)'''
    if height_for_yellow + 2 > height > height_for_yellow - 2:
        print("code workedasdfghjdsgfaBGFDSHEhgSAfdSghfxkjreshtewa")
        break
#Initializes the height for the yellow keyhole
drone.set_throttle(50)
<<<<<<< Updated upstream
drone.move(2)
drone.set_throttle(0)
drone.set_pitch(80)
drone.move(2.1)
=======
drone.move(1)
drone.set_throttle(0)
print("Correct height, moving forward!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#Moves forward through the yellow keyhole
drone.set_pitch(80)
drone.move(1.8)
>>>>>>> Stashed changes
print("I'm Forward")
#Goes down to the green keyhole height
drone.set_pitch(0)
drone.set_throttle(-50)
<<<<<<< Updated upstream
drone.move(0.5)
print("I'm Down")
=======
drone.move(0.6)
>>>>>>> Stashed changes
print("I'm Down!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#This moves it sideways, through the green keyhole
drone.set_throttle(0)
drone.set_pitch(0)
<<<<<<< Updated upstream
##drone.set_roll(60)
drone.move(0.3)
print("I'm Right")
drone.set_throttle(0)
drone.set_pitch(0)
#drone.set_roll(-80)
#drone.move(0.5)
print("I'm Right")
drone.set_throttle(0)
drone.set_pitch(0)
drone.set_roll(50)
drone.move(2)
# drone.set_roll(80)
# drone.move(1.2)
# print("I'm Right")
drone.set_pitch(-20)
drone.move(1)
print("I'm landing")
#drone.spiral(50, 5, 1)
=======
drone.set_roll(80)
drone.move(1.05)
print("I'm Right")
#Moves it backwards to initialize the landing
drone.set_pitch(-10)
drone.move(0.5)
#Lands
print("I'm landing")
>>>>>>> Stashed changes
drone.land()