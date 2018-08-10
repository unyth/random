def bubble_sort(n_list):
	while(True):
		swap = 0
		for i in xrange(1,len(n_list)):
			if n_list[i-1] > n_list[i]:
				n_list[i-1], n_list[i] = n_list[i], n_list[i-1]
				swap +=1
		if swap == 0:
			break
	return n_list
