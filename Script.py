# Importing libraries
import sys

# Getting the input from command
n=int(sys.argv[1])
# Deciding if the number is even or odd by taking its modulus 2
if n%2==0:
	print("Es par!")
else :
	print("Es impar...")
