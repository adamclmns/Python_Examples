#Python 3.3.3
#RockPaperScissors.py

#Working on this one to become a fairly intelligent 
#score-keeping game. Will tie in with other programs eventually.
#9/24/13
import time
import random

print("Let's Play a game!")
print("I really like Rock Paper Scissors")
time.sleep(1)
MyChoice=random.randint(1,3)

print("1 for Rock, 2 for Scissors, and 3 for Paper!")
time.sleep(2)

print("ready?")
time.sleep(1)
print("Rock...")
time.sleep(1)
print("Paper...")
time.sleep(1)
print("Scissors...")
time.sleep(1)

Check=0
while(Check!=1):
	YourChoice=int(raw_input("SHOOT!"))
	if(YourChoice>3):
		print("Try again... between 1 and 3")
	elif(YourChoice<1):
		print("Try Again... between 1 and 3")
	else:
		Check=1

#1 = Rock
#2 = Scissors
#3 = Paper



if(MyChoice==1):#Computer picked Rock
	MyChoice="Rock"
	if(YourChoice==1):
		YourChoice="Rock"
		print("TIE")
	elif(YourChoice==2):
		YourChoice="Scissors"
		print("You lose!")
	elif(YourChoice==3):
		YourChoice="Paper"
		print("YOU WON!")
elif(MyChoice==2):#Computer Picked Scissors
	MyChoice="Scissors"
	if(YourChoice==1):
		YourChoice="Rock"
		print("YOU WON!")
	elif(YourChoice==2):
		YourChoice="Scissors"
		print("TIE")
	elif(YourChoice==3):
		YourChoice="Paper"
		print("You lost")
elif(MyChoice==3):#Computer picked Paper
	MyChoice="Paper"
	if(YourChoice==1):
		YourChoice="Rock"
		print("You lose!")
	elif(YourChoice==2):
		YourChoice="Scissors"
		print("YOU WON!")
	elif(YourChoice==3):
		YourChoice="Paper"
		print("TIE")
		
print "Computer Chose: ",MyChoice
print "You chose: ",YourChoice
