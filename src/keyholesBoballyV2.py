from BaseCode import BRBDrone
drone = BRBDrone()
drone.pair()

if drone.battery_check_takeoff():
    drone.takeoff()
    drone.height_correction(90)
    drone.simple_move(55,0,80,0, 1.2)
    drone.simple_move(75,0,-60,0, 1.05)
    print("HOOP 1 DONE")
    drone.simple_move(0,75,0,0, 2.5)
    # drone.simple_move(0,-75,0,0, 1)
    # drone.simple_move(-75,0,60,0, 1.2)
    # drone.simple_move(75,0,-60,0, 1.2)
    # drone.simple_move(0,75,0,0, 2)
#     drone.simple_move(75,0,-40,0, 1)
#     drone.simple_move(0,75,0,0, 1)
# else:
    drone.land()

