# Tyler High
# Rock, Paper, Scissors
#######################
# Welcome Message
# 1. Print a welcome message.
# 2. Promps for a name
# change this
# Game Loop
# Print score
# Prompt for player choice
# Get the computer choice (random)
# Compare
# Print results
# Change score variable

# Score Screen
# Print "Score: "
# Print the player score using the name
# Print the computer score
import random
# VARIABLES
pScore = 0
cScore = 0
ties = 0
computerChoices = ["rock", "paper", "scissors"]


#WELCOME MESSAGE
print("Welcome to Rock, Paper, Scissors!")
playerName = input("What is your name?: ")


#PRINT SCORE
def printScore():
	print("The score is: ")
	print(playerName + ": " + str(pScore))
	print("Computer: " + str(cScore))
	print("Ties: " + str(ties))

#GAME LOOP
while True:
	# print the score
	printScore()
	# prompt for player choice
	pChoice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' to quit the game: ")
	# get the computer choice (random)
	cChoice = random.choice(computerChoices)
	# compare
	# compare pChoice to 'q'
	# 1. break out of the list 
	if pChoice == "q":
		break 
	# compare pChoice to 'r'
	# compare rock to computer choice
	elif pChoice == "r":
		print("You picked rock")
		if cChoice == "rock":
			print("Computer picked rock")
			print("This is a tie")
			ties = ties + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("Computer has won this round.")
			cScore = cScore + 1
		else: # scissor is only one left
			print("Computer picked scissors")
			print(playerName + "h as won this round.")
			pScore = pScore + 1
	# compare pChoice to 'p'
	elif pChoice == "p":
		print("You picked paper")
		if cChoice == "rock": 
			print("Computer picked rock")
			print(playerName + " has won this round.")
			pScore = pScore + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("This is a tie")
			ties = ties + 1
		else:
			print("Computer picked scissors")
			print("Computer has won this round")
			cScore = cScore + 1
	# compare pChoice to 's'
	elif pChoice == "s":
		print("You picked scissors")
		if cChoice == "rock":
			print("Computer picked rock")
			print("Computer has won this round.")
			cScore = cScore + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print(playerName + " has won this round")
			pScore = pScore + 1
		else:
			print("Computer picked scissors")
			print("This is a tie")
			ties = ties + 1 
	# compare pChoice to everything else
	else:
		print("You picked an invalid key.")
	# print results
	# change score variable