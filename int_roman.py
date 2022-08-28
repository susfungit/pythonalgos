"""
converts integer to roman equivalent
There are 7 literals in Roman
I, V, X, L, C, D and M.

I	1
V	5
X	10
L	50
C	100
D	500
M	1000

In addition there are some literals used for specific numbers
to represent 4 (which is obtained by subtracting 1 from 5) we use IV
to represent 9 we use IX... so following additional representations need to be considered

IV	4
IX	9
XL	40
XC	90
CD	400
CM	900
"""
def IntToRoman(n):
	nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
	romans=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
	num=n
	result=''
	for i in range(len(nums)):
		div=num//nums[i]
		if div:
			result=result +romans[i]*div
			num=num%nums[i]	
	return result
