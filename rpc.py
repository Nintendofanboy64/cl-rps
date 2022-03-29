import random  
import sys
x = True

def game():
	weapons =["", "Rock", "Paper", "Scissors"]
	print("\033[1;32;40m")
	print(weapons[1:])
	print("\033[1;32;40m\nRock = 1", "Paper = 2", "Scissors = 3\n")

	choice = input("Choose your weapon: ")
	num_choice = int(choice)

	computer = random.choice(weapons)
	num_computer = int(weapons.index(computer))

	print(weapons[num_choice] + " Vs " + computer)

	if num_choice == num_computer:
		print("\033[1;36;40mDraw")
		play()

	elif num_choice == 1 and num_computer == 3:
		print("\033[1;33;40mWin!!!!")
		play()

	elif num_choice == 1 and num_computer == 2:
		print("\033[1;31;40mYou Lose :(")
		play()

	elif num_choice == 2 and num_computer == 3:
		print("\033[1;31;40mYou Lose :(")
		play()
	
	elif num_choice == 2 and num_computer == 1:
		print("\033[1;33;40mWin!!!!")
		play()

	elif num_choice == 3 and num_computer == 2:
		print("\033[1;33;40mWin!!!!")
		play()

	elif num_choice == 3 and num_computer == 1:
		print("\033[1;31;40mYou Lose :(")
		play()

	else:
		print("\033[1;36;40moops daisy yay")
		print("\033[1;36;40mThe computer chickened out due to anxiety")
		play()

def play():
	game = input("Do you want to play? (yes or no): ")
	if game == "yes":
		x = True

	else:
		x = False
		sys.exit(0)

while x:
	game()
