# By Abdullahi Farah
#
# Problem 2:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#

def solve():
	sum = 0
	initialValue = 1
	nextValue = 1
	thirdValue = initialValue+nextValue
	count = 4000000
	while thirdValue < count:
		sum += thirdValue
		initialValue = nextValue + thirdValue
		nextValue = initialValue + thirdValue
		thirdValue = nextValue + initialValue
	return sum

print solve()