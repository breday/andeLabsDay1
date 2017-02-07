#code starts here
def data_type(n):
	#check if n is a list ,then do_something
	if isinstance(n, list):
		if len(n) < 3:
			return None
		else:
		    return data[2]

	#check if  n is int,then do something 
	if isinstance(n, int):
		if n == 100:
			return "equals to 100"
		elif n < 100:
			return "less than 100"
		else:
			return "more than hundred"

	#check if n is ,bool or str or no value
	if type(n) == None:
		return "no value "
	elif type(n) == bool:
		return n
	else:
		type(n) == str
		return len(n)	

#print outcome
print(data_type(7))