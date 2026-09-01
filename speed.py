#Speed Checker
speed = int(input("Enter the speed of the vehicle:"))

if speed > 100:
    print("Vehicle is overspeeding")
elif 60 <= speed <= 100:
    print("Vehicle is moving in normal speed")
else:
    print("Vehicle is moving in slow speed")
