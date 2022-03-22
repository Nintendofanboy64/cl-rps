import random  

weapons =["", "Rock", "Paper", "Scissors"]

print(weapons)
print("Rock = 1", "Paper = 2", "Scissors = 3")

choice = input("Choose your weapon: ")
num_choice = int(choice)

computer = random.choice(weapons)
num_computer = int(weapons.index(computer))

print(weapons[num_choice] + " Vs " + computer)

if num_choice == num_computer:
    print("Draw")

elif num_choice == 1 and num_computer == 3:
    print("Win!!!!")

else:
    print("oops daisy yay")
