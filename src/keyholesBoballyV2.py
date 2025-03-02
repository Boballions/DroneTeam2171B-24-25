from BaseCode import BRBDrone
drone = BRBDrone()
drone.pair()
drone.set_drone_LED(0, 225, 0, 100)  # Blue
if drone.battery_check_takeoff():
    drone.takeoff()
    what_color = input("What color B,R,or G")
    if what_color == "B":
        drone.set_drone_LED(0, 0, 225, 100)
    elif what_color == "R":
        drone.set_drone_LED(225, 0, 0, 100)
    else:
        drone.set_drone_LED(0, 225, 0, 100)
    drone.height_correction(90)
    drone.simple_move(55,-10,80,0, 1.4)
    drone.simple_move(80,0,-40,0, 1.05)
    print("HOOP 1 DONE")

    drone.simple_move(0,75,-30,0, 2.5)
    while drone.get_height()>100:
        drone.simple_move(0,20,0,0,0.2)
    drone.land()
else:
    drone.land()

