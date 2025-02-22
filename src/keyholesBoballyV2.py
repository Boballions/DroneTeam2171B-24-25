from BaseCode import BRBDrone
drone = BRBDrone()
drone.pair()

if drone.battery_check_takeoff():
    drone.takeoff()
    drone.height_correction(90)
    drone.simple_move(55,0,85,0, 1.2)
    drone.simple_move(75,0,-60,0, 1.05)
    print("HOOP 1 DONE")

    drone.simple_move(0,75,-30,0, 2.5)
    while drone.get_height()>100:
        drone.simple_move(0,20,0,0,0.2)
    drone.land()
else:
    drone.land()

