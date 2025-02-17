from codrone_edu.drone import *
from BaseCode.py import *
drone = Drone()
drone.pair()
drone.takeoff()

drone.battery_check_takeoff()
drone.get_height(100)
drone.find_color()

#Goes through the two arches
for i in range(2):
    drone.simple_move(55,0,0,0,3)
    drone.simple_move(-55,0,0,0,1.6)
    drone.get_height(100)
    drone.simple_move(0,0,55,0,1.8)
    drone.simple_move(50,0,0,0,1.2)
    drone.simple_move(0,0,-100,0,1.2)
    drone.simple_move(-60,0,0,0,1.75)
    drone.simple_move(0,0,100,0,1.2)
    drone.simple_move(-50,0,0,0,1.3)
    drone.simple_move(0,0,-100,0,0.75)
    drone.simple_move(31,0,0,0,1.5)
    drone.return_home()
    drone.get_height(100)
drone.get_height(70)
drone.simple_move(60,0,0,0,4)
drone.simple_move(-60,0,0,0,1)
drone.simple_move(60,0,0,0,1)
