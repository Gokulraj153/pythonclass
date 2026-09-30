import random
number = random.randint(1,10)
attempt = 0
while True:
    query = int(input("Enter your guess"))
    if query == number:
        attempt+=1
        print("Correct!")
        print(f"You guessed the number in {attempt} attemps")
        break
    else:
        if query > number:
            print("Too high!")
            attempt+=1
        elif query < number:
            print("Too Low!")
            attempt+=1