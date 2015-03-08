import math

def primes(maxValue):
	A = [True]*(maxValue+1)
	A[0] = False
	A[1] = False
	for i in range(2,int(math.sqrt(maxValue))):
		if A[i]:
			for j in range(0, maxValue):
				index = i**2 + j*i
				if index > maxValue:
					break
				A[index] = False
 
	for i in range(0,len(A)):
		if A[i]:
			yield i

def level10():
	return sum(primes(2000000))
	
if __name__ == "__main__":
	print level10()