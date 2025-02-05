from codrone_edu.drone import *

drone = Drone()
drone.pair()

def showBattery():
    Red = 100
    Blue = 100
    Green = 100
    battery = drone.get_battery()
    drone.set_drone_LED(Red, Blue, Green, battery)
print("Temperature is: ", drone.get_drone_temperature())
print("Pressure is: ", drone.get_pressure())
print("Battery is: ", drone.get_battery())
print("Angle is: ", drone.get_angle_x(), drone.get_angle_y(), drone.get_angle_z())
showBattery()
drone.close()