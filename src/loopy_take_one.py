from codrone_edu.drone import *
drone=Drone()
drone.pair()

drone.load_color_data("color_data")

for i in range(100):

    color_data = drone.get_color_data()

    color = drone.predict_colors(color_data)

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
#The above code sets the color sensor and loads all of the data.

drone.takeoff()

drone.set_pitch(50) #goes forward to second arch
drone.move(3)
drone.set_pitch(0)
drone.set_throttle(50)#flies above second arch
drone.move(4.5)
drone.set_throttle(0)
drone.set_pitch(50) #goes through second arch
drone.move(1.5)
drone.set_pitch(0)
drone.set_throttle(-50)#goes down to fly under second arch
drone.move(1)
drone.set_throttle(0)
drone.set_pitch(-50) #goes backwards to first arch
drone.move(0.5)
drone.set_pitch(0)
drone.set_throttle(50)#goes above first arch
drone.move(4.2)
drone.set_throttle(0)
drone.set_pitch(-50) #flies above first arch
drone.move(2)
drone.set_pitch(0)
drone.set_throttle(-50)#goes down
drone.move(4)
drone.set_throttle(0)
drone.set_pitch(50)#goes forward to get credit
drone.move(4)
drone.set_pitch(0)


drone.land()
drone.close()