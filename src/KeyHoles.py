from BaseCode import BRBDrone

drone = BRBDrone()
drone.pair()
drone.PID_Setup()
drone.battery_check_takeoff()
drone.find_color()
drone.height_correction(128)
drone.PID_Setup()
drone.simple_move(0,0,50,0, 2)
drone.simple_move(80,0,0,0,2.1)
# drone.simple_move(80,0,0,0,3.6)
# drone.simple_move(0,0,-50,0,1.7)
# drone.simple_move(0,50,0,0,2)
# drone.simple_move(-20,50,0,0,1)

drone.land()
