import random
playing=True
number=str(random.randint(0, 9))

print("I will genrate a number from 0 to 9< and you have to guess the numberone digit a time.")
print("The Game ends when you get 1 HERO!!!")

while playing:
    guess= input("Give me your best guess! \n")
    if number == guess:
        print("You Win the game!!!")
        print("The Number was ", number)
        break
    else:
        print("Yor guess isn't quite right, try again.\n")