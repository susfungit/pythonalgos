def is_prime(no):
	return (no==1) or len([i for i in range(2,no//2+1) if no%i ==0]) == 0 

