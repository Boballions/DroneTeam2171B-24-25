from BaseCode import BRBDrone
drone = BRBDrone()
drone.pair()

if drone.battery_check_takeoff():
    drone.takeoff()
    drone.height_correction(90)
    # drone.find_color()

    #Goes through the two arches
    for i in range(1):
        #Forward Under Ar
        drone.simple_move(0,0,-100,0,0.5)
        drone.simple_move(80,0,0,0,2.5)
        drone.hover(2)
        #Back TO start
        drone.simple_move(-80,0,0,0,2.5)
        drone.hover(2)
        drone.simple_move(80,0,80,0,2)
        drone.simple_move(0,0,-90,0,1.3)
        drone.simple_move(-80,0,20,0,2)
        drone.simple_move(0,0,-90,0,0.8)
        drone.simple_move(80,0,20,0,2)
        drone.simple_move(0,0,-90,0,1.3)
        drone.simple_move(-80,0,20,0,2)
        drone.simple_move(0,0,-90,0,0.8)
else:
    drone.land()