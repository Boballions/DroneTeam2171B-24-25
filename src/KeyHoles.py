from BaseCode import BRBDrone

drone = BRBDrone()
drone.pair()
drone.PID_Setup()
drone.battery_check_takeoff()
drone.find_color()
drone.height_correction(90)
drone.PID_Setup()
drone.simple_move(0,0,100,0,1)
drone.PID_Move(0,0,2.1)
print("lkjasflkjaflkj")
drone.hover(0.5)
drone.PID_Move(2.1,0,1.6)
drone.hover(0.5)
drone.PID_Move(2,-2.0,0.8)
# drone.simple_move(10,0,0,0,0.5)
# drone.hover(0.5)
# drone.simple_move(-10,0,0,0,0.5)
# drone.hover(0.5)
# drone.PID_Move(2,0,1.4)
# drone.hover(0.5)
# drone.PID_Move(2,-2,0.4)
# drone.PID_Move(2,0,0.6)

# drone.height_correction(90)
# drone.PID_Move(1,0,2)
drone.land()