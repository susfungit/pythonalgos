"""
converts integer to roman equivalent
"""
class Solution(object):
	def IntToRoman(self,n):
		
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
obj1=Solution()
print(obj1.IntToRoman(2974))
