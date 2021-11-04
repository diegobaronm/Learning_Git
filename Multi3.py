# Importing libraries
import sys

# Getting the input from command
n=int(sys.argv[1])
# Defining function to decide if a number is a multiple of 3
def Multi3(n):
	if n%3==0:
		print("El numero "+str(n)+" es multiplo de 3!")
	else :
		print("El numero "+str(n)+" no es multiplo de 3...")

# This is the main part of the program!
Multi3(n)
