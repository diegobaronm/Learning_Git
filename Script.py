# Importing libraries
import sys

# Getting the input from command
n=int(sys.argv[1])
# Defining function to decide parity of a number

def odd_vs_even(n):
	if n%2==0:
		print("El numero "+str(n)+" es par!")
	else :
		print("El numero "+str(n)+" es impar...")

odd_vs_even(n)
