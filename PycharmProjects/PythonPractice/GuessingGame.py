import random

name=input("Hey, Your Name please?\t ")
print("Hello, "+name)

print("I have an interesting game for you!")
rd = random.randint(1,9)


guess = 0
c = 0

while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9\t")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")
input()