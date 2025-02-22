from BaseCode import BRBDrone

drone = BRBDrone()
drone.pair()


if drone.battery_check_takeoff():
    drone.takeoff()
    drone.height_correction(90)
    # drone.load_color_data("color_data")
    #
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

    # Moves up before going through the 2 arches
    #Goes through the two arches
    for i in range(1):
        #Forward Under Ar
        drone.simple_move(0,0,100,0,0.6)
        drone.simple_move(80,0,0,0,2.5)
        drone.hover(0.2)
        drone.simple_move(-80,0,0,0,2.3)
        drone.hover(0.2)
        # Start Figure 8
        drone.simple_move(60,0,0,0,0.2)
        drone.simple_move(60,0,50,0,2)
        drone.simple_move(60,0,0,0,0.5)
        drone.simple_move(0,0,-80,0,1)
        drone.simple_move(-90,0,0,0,0.3)
        drone.simple_move(-60,0,50,0,2)
        drone.simple_move(-60,0,0,0,0.5)
        # drone.simple_move(-80,0,20,0,2)
        # drone.simple_move(0,0,-90,0,0.8)
        # drone.simple_move(80,0,20,0,2)
        # drone.simple_move(0,0,-90,0,1.3)
        # drone.simple_move(-80,0,20,0,2)
        # drone.simple_move(0,0,-90,0,0.8)
else:
    drone.land()