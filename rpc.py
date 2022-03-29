import random  
import sys
x = True

def game():
	weapons =["", "Rock", "Paper", "Scissors"]
	print("")
	print(weapons[1:])
	print("\nRock = 1", "Paper = 2", "Scissors = 3\n")

	choice = input("Choose your weapon: ")
	num_choice = int(choice)

	computer = random.choice(weapons)
	num_computer = int(weapons.index(computer))

	print(weapons[num_choice] + " Vs " + computer)

	if num_choice == num_computer:
		print("Draw")

	elif num_choice == 1 and num_computer == 3:
		print("Win!!!!")
		
	elif num_choice == 1 and num_computer == 2:
		print("You Lose :(")

	elif num_choice == 2 and num_computer == 3:
		print("You Lose :(")
		
	elif num_choice == 2 and num_computer == 1:
		print("Win!!!!")
		
	elif num_choice == 3 and num_computer == 2:
		print("Win!!!!")
		
	elif num_choice == 3 and num_computer == 1:
		print("You Lose :(")

	else:
		print("oops daisy yay")
		print("The computer chickened out due to anxiety")

def play():
	game = input("Do you want to play? (yes or no): ")
	if game == "yes":
		x = True

	else:
		x = False
		sys.exit(0)

while x:
	game()