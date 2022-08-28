"""
A number that is > 1 is prime if its only divisor is itself. 
The following algorithm is_prime uses list comprehenssions to build all the divisors of number upto its half and then checks if it is empty.. 
If there were no divisors upto half the numberthen we are guranteed to have no further divisors . i
 This is inefficient algorithm as it always goes up to half the number .  Ideally we should exit the loop as soon as divisor is found ..i

 Also more efficient is if we don't find any divisor upto numbers square root, we are guranteed that number is prime. So for example for 113 it is enough to loop only upto 12 rather than following algo which loops to 57
"""

import math

def is_prime(no):
	if no <=1 :
		return False
	if no > 2 and no%2 == 0:
		return False

	return True if len([i for i in range(3,no//2+1,2) if no%i ==0]) == 0  else False



def is_prime_number(no):
	if (no <=1) or (no > 2 and no %2==0):
		 return False
	is_prime_no= True
	i=3
	while i <= int(math.sqrt(abs(no))):
		if no % i== 0:
			is_prime_no=False
			break
		i+=2	
	return is_prime_no

print(is_prime_number(62))
print(is_prime_number(67))
print(is_prime_number(144))
print(is_prime_number(2000))
