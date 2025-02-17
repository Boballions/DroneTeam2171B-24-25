from BaseCode import *
drone = Drone()
drone.pair()
drone.takeoff()

if drone.battery_check_takeoff():
    drone.get_height(100)
    drone.find_color()
    drone.simple_move(0,0,50,0,2.2)
    drone.simple_move(80,0,0,0,4)
    drone.simple_move(0,0,-50,0,1.7)
    drone.simple_move()
