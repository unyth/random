import random

n = input() #let user input a number of their choice
if n == 0: n = int(random.random() * 1000000000) #if user give up choice

count_1 = 0

for i in xrange(0,n):
	temp = str(i)
	if temp[0] == '1':
		count_1 += 1

print(float(count_1)/n)
