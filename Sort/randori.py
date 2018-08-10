import random

def n_list(n):
	nl = [] #int list to be returned
	
	#creating a list of integers from 1 to n
	for i in xrange(1,n+1):
		nl.extend([i])
	
	#shuffle the list of integers into random order
	#to the best ability of python prng
	while n > 1:
		choice = int(random.random()*n)
		pick = nl.pop(choice)
		nl.extend([pick])
		n -= 1

	return nl
