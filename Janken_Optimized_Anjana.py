#Janken by ANJANA

#Initialize
import os
import random
import time
os.system ("clear")
print ("""
               __
  | /\ |\ ||_/|_ |\ |
__)/--\| \|| \|__| \|
""")

name = raw_input("Hello, what's your name? >> ")
print ""
print ("Okay " + name + """, here are the rules.
Just follow the simple rules of Janken.
Scissors wins paper.
Paper wins rock.
Rock wins scissors.

First to reach 3 wins is the overall winner.""")
raw_input ("OK???  > ")
print ("")
#Let the computer make a choice

#Get a choice from the user

user_wins = 0
comp_wins = 0

while True:
	user_choice = raw_input("""
Please choose the following:
	R) Rock
	S) Scissors
	P) Paper
	""")
	user_choice = user_choice.upper()

	computer_choice = random.randint(1,3)
	if computer_choice == 1:
		computer_choice = "R"
	elif computer_choice == 2:
		computer_choice = "P"
	elif computer_choice == 3:
		computer_choice = "S"

	print ("Sai")
	time.sleep (0.1)
	print ("Sho wa")
	time.sleep (0.1)
	print ("Gu")
	time.sleep (0.2)
	print ("Janken")
	time.sleep (0.4)
	print ("Poi!!")

	if computer_choice == "R":
		print """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


	The computer chose rock. So...
		"""

	elif computer_choice == "P":
		print """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

	The computer chose paper. So...
		"""
	elif computer_choice == "S":
		print """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

	The computer chose scissors. So...
		"""

	#User wins
	#Computer: R    User: P
	#Computer: P    User: S
	#Computer: S    User: R
	if (computer_choice == "S" and user_choice == "R") or \
		(computer_choice == "P" and user_choice == "S") or \
		(computer_choice == "R" and user_choice == "P"):
		print (" You win " + name + ", hooray! ")
		user_wins = user_wins + 1


	#Computer wins
	#Computer: R    User: S
	#Computer: P    User: R
	#Computer: S    User: P
	if (computer_choice == "R" and user_choice == "S") or \
		(computer_choice == "S" and user_choice == "P") or \
		(computer_choice == "P" and user_choice == "R") :
		print ("You lose, " + name + "." )
		comp_wins = comp_wins + 1

	#Tie
	#Computer: R    User: R
	#Computer: P    User: P
	#Computer: S    User: S
	if user_choice == computer_choice:
		print ("Whoaaa, it's a tie! Try again.")

	user_choice = user_choice.upper()
	if user_choice != "R" and user_choice != "S" and user_choice != "P":
		print "Read the directions! You didn't choose [R]ock, [P]aper or [S]cissors!"


	if user_wins == 3:
		print ("3 wins, " + name + "! You win!")
		break
	if comp_wins == 3:
		print ("The computer won 3 times, " + name + "! Game over!")
		break

	if user_wins - comp_wins == 1:
		print ("Leading, huh " + name + "? Be careful, you're only a point ahead.")

	elif user_wins - comp_wins == 2:
		print ("Leading, huh " + name + "? You can relax because you're two points ahead!")

	if user_wins - comp_wins == -1:
		print ("Catch up " + name + "! You're only a point behind!")

	if user_wins - comp_wins == -2:
		print ("Catch up " + name + "! You're two points behind!")

	if user_wins - comp_wins == 0 and user_wins != 0 :
		print ("You are battling at " + str(user_wins) + " vs " + str(comp_wins) + " now! Get a lead in the next round!")

	play_again = raw_input ("Do you want to play again? Yes or No >> ")
	print ""
	if play_again == "No" or play_again == "no":
		break
	else:
		continue

print ("Thanks for playing!")
