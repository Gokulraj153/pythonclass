Letter = input("Enter the letter: ")

match (Letter):
    case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
        print("It is a vowel")
    case _:
        print("It is a consonant letter")
