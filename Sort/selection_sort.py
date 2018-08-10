#Assume a list is the input

def selection_sort(n_list):
	for i in xrange(1,len(n_list)):
	    for j in xrange(0,i):
	    	if n_list[i] < n_list[j]:
	    		n_list[i], n_list[j] = n_list[j], n_list[i]
	return n_list

