from BaseCode import BRBDrone

drone = BRBDrone()

drone.pair()


while True:
    drone.simple_move(0, 0, 100, 0, 1)
    drone.PID_Move(0, 0, 1)
    drone.simple_move(0, 0, 100, 0, 1)
    drone.PID_Move(0, 0, 0)