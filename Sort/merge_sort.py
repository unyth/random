#Assume the input is a list

def merge_sort(n_list):
	n = len(n_list)
	
	#base case
	if n == 1:
		return n_list
	
	#Divide and Conquer
	right = merge_sort(n_list[0:n/2])
	left = merge_sort(n_list[n/2:])

	#Merge step
	return merge(right,left)


def merge(right, left):
	#eventually list of the merged
	result = []

	#right or left are non-empty
	while (right or left):
		while (right and left):
			if right[0] < left[0]:
				result.append(right.pop(0))
			else:
				result.append(left.pop(0))
		if right:
			result.append(right.pop(0))
		else:
			result.append(left.pop(0))
	return result
