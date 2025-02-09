from codrone_edu.drone import *
drone = Drone()
drone.pair()


height = drone.get_height()
drone.calibrate()
drone.takeoff()
drone.hover(2)
print(-height)
drone.land()
drone.close()