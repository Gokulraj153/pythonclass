day = input("Enter the day: ")
match(day):
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" :
        print("It is a Weekdays")
    case "Saturday" | "Sunday":
        print("It is a Weekends")
