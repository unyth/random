from random import shuffle

l = [x for x in xrange(0,100)]
shuffle(l)
print(l)

from selection_sort import selection_sort 
print(selection_sort(l))


