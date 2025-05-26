from BaseCode import BRBDrone

drone = BRBDrone()

drone.pair()
# drone.takeoff()
tunningZ = True
tunningX = True
tunningY = True
ZKp = 100
ZKi = 1.5
ZKd = 0.1
XKp = 80
XKi = 0.1
XKd = 0.03
YKp = 80
YKi = 0.1
YKd = 0.03
while tunningZ:
    drone.land()
    ZKp = float(input("Your current ZKp is " + str(ZKp) + " what do you want it to be? "))
    ZKi = float(input("Your current ZKi is " + str(ZKi) + " what do you want it to be? "))
    ZKd = float(input("Your current ZKd is " + str(ZKd) + " what do you want it to be? "))
    drone.PID_Setup(ThrottleKp = ZKp, ThrottleKi = ZKi, ThrottleKd = ZKd)
    drone.takeoff()
    drone.PID_Move(0,0,1)
    print(drone.get_position_data()[3])
    done = input("Are you done(y or n)? ")
    if done == "y":
        tunningZ = False
while tunningX:
    drone.land()
    XKp = float(input("Your current XKp is " + str(XKp) + "what do you want it to be? "))
    XKi = float(input("Your current XKi is " + str(XKi) + "what do you want it to be? "))
    XKd = float(input("Your current XKd is " + str(XKd) + "what do you want it to be? "))
    drone.PID_Setup(PitchKp = XKp, PitchKi = XKi, PitchKd = XKd)
    drone.PID_Move(0,0,1)
    drone.hover(100)
    drone.PID_Move(1,0,1)
    print(drone.get_position_data()[2])
    done = input("Are you done(y or n)? ")
    if done == "y":
        tunningX = False
while tunningY:
    drone.land()
    YKp = float(input("Your current YKp is " + str(YKp) + "what do you want it to be? "))
    YKi = float(input("Your current YKi is " + str(YKi) + "what do you want it to be? "))
    YKd = float(input("Your current YKd is " + str(YKd) + "what do you want it to be? "))
    drone.PID_Setup(RollKp = YKp, RollKi = YKi, RollKd = YKd)
    drone.PID_Move(0,0,1)
    drone.hover(100)
    drone.PID_Move(0,1,1)
    print(drone.get_position_data()[1])
    done = input("Are you done(y or n)? ")
    if done == "y":
        tunningY = False
