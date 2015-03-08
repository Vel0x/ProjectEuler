def level10():
	primes = [2]
	i = 3
	while True:
		isPrime = True
		for p in primes:
			if i%p == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(i)
		i += 2
		if i > 2000000:
			return sum(primes)
					
if __name__ == "__main__":
	print level10()