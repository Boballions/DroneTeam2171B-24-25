from BaseCode import BRBDrone

drone = BRBDrone()
drone.pair()
drone.PID_Setup()
drone.battery_check_takeoff()
drone.find_color()
drone.height_correction(90)
drone.PID_Setup()
#Fly to yellow hoop
drone.simple_move(0, 0, 100, 0, 1)
drone.PID_Move(0, 0, 2.1)
drone.simple_move(100, 0, 0, 0, 0.3)
drone.simple_move(-100, 0, 0, 0, 0.3)
print("Correct Hight")
drone.hover(0.5)
#Fly Through Green Hoop
drone.PID_Move(2.1 ,0, 1.6)
drone.simple_move(9, 100, 0, 0, 0.3)
drone.simple_move(0, -100, 0, 0, 0.3)
drone.hover(0.5)
# Fly to box
drone.PID_Move(2, -2, 1)
while drone.get_height()>100:
  drone.simple_move(0,20,0,0,0.2)
drone.land()
drone.land()
