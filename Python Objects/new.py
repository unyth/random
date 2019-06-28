class A(object):
	def __new__(cls):
		print("A.__new__ called")
	def __str__(self):
		return "Class A"

class C(object):
	def __new__(cls):
		print "C.__new__ is called"
		# return super(C, cls).__new__(A)
		print dir(cls)
		return object.__new__(A)

	def __init__(self):
		print "C.__init__ is called"

if __name__ == "__main__":
	print("Calling Main")

	A = C()
	print(A)