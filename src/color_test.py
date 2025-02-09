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





