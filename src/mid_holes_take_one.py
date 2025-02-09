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




drone.takeoff()
drone.set_throttle(50)
drone.move(1.3)#moves up to hole height
drone.set_throttle(0)
drone.set_pitch(50)
drone.move(3.9)#moves forward through green hole
drone.set_pitch(0)
drone.set_roll(50)
drone.move(2)#moves sideways through yellow hole
drone.land()
drone.close()