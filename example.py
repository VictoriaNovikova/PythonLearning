def get_sum(first, second):
	if isinstance(first, (int, float)) and isinstance(second, (int, float)):
		return first + second
	else:
		return str(first) + str(second)

	

print(get_sum("Hello", 3))
print(get_sum("Hello ", "world"))
print(get_sum(2, 3.4))
print(get_sum(5, "fff"))



def get_summ(one, two, delimeter=' '):
	return (str(one) + str(delimeter) + str(two)).upper()

print(get_summ(1, 3.4, ", "))
print(get_summ("Hello" , 3.14, ", "))