import sys

n=int(sys.argv[1])

def odd_vs_even(n):
	if n%2==0:
		print("El numero "+str(n)+" es par!")
	else :
		print("El numero "+str(n)+" es impar...")

odd_vs_even(n)
