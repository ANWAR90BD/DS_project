

# def check(my_string):
# 	brackets = ['()', '{}', '[]']
# 	while any(x in my_string for x in brackets):
# 		for i in brackets:
# 			my_string = my_string.replace(i, '')
# 	return not my_string


# string = "{[]{()}}}"
# print(string, "-", "True"
# 	if check(string) else "False")


x = []
y = "(", "(", ")", ")"

def valid(x, y):
	for i in range(len(y)):
		result = y[i]
	if result == "(":
		x.append(result)
	elif result == ")":
		x.pop(result)
		if result == 0:
			return True
		else:
			return False
	return x

print(valid(x, y))
	
	