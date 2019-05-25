# coding: utf-8

import random
	

print("••••• THE GREAT AZBARIX •••••")
print("• presents his famous trick •")
print("••••• The Magic Number ••••••")

print("\b")

print("\"i am thinking of a number")
print(" from 1-8. i want you to guess")
print(" that number and i’ll tell you")
print(" if it’s higher or lower.")
print(" you have three guesses.\"")
print("\b")

def taunt():
	x = ("BWAHAHA! the answer was %s!" % x)
	y = "hy"
	z = "ho"
	taunt = [x,y,z]
	n = random.randint(0,2)
	return(taunt[n])

#taunt()

a = raw_input("what’s your first guess?: ")

if a > str(4):
	print("ha! the number is lower than %s!" % a)
	print("\b")
	b = raw_input("guess again: ")
	if b > str(2):
		print("too high")
		c = raw_input("last guess: ")
		if c > str(1):
			print("BWAHAHA! the answer was 1!")
			print("You make Azbarix look great!")
		elif c < str(2):
			print("You look like a FOOL!")
			print("the answer is 2. you lose!")
	elif b < str(3):
		print("too low")
		c = raw_input("last guess: ")
		if c > str(3):
			print("You embarrass yourself.")
			print("the answer is 3. you lose!")
		elif c < str(4):
			print("I win again!")
			print("the answer is 4. you lose!")
elif a < str(6):
	print("too low")
	b = raw_input("guess again: ")
	if b > str(6):
		print("too high")
		c = raw_input("last guess: ")
		if c > str(5):
			print("Azbarix never loses!")
			print("the answer is 5. you lose!")
		elif c < str(6):
#			print(taunt())
			print("the answer is 6. you lose!")
	elif b < str(7):
		print("too low")
		c = raw_input("last guess: ")
		if c > str(7):
			print("the answer is 7. you lose!")
		elif c < str(8):
			print("the answer is 8. you lose!")

