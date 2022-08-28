def reverse(x:int)->int:
	sign=1 if x else -1
	num=abs(x)
	result=0
	while num:
		result=result*10 + num%10
		num=num//10
	return 0 if result > pow(2,31) else sign * result


def is_palindrome(x:int)->bool:
	return False if x < 0 else x==reverse(abs(x))

print(is_palindrome(-2212))
