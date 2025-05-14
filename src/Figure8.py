from BaseCode import BRBDrone

drone = BRBDrone()
drone.pair()
drone.battery_check_takeoff()
drone.find_color()
drone.height_correction(90)
drone.PID_Setup()

drone.land()
