from codrone_edu.drone import *

drone = Drone()
drone.pair()
drone.takeoff()
drone.set_pitch(50)
drone.move(0.5)
drone.land()
drone.close()