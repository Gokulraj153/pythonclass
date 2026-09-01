signal = input("Enter the signal:")

match(signal):
    case "Red" | "red":
        print("Stop the Vehicle")
    case "Yellow" | "yellow":
        print("Slow down the Vehicle")
    case "Green" | "green":
        print("You can Go")
