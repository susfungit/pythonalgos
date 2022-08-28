class Solution:
	def uniqueMorseRepresentations(self, words: list[str]) -> int:
		morseTable = {
			"a":".-",
			"b":"-...",
			"c":"-.-.",
			"d":"-..",
			"e":".",
			"f":"..-.",
			"g":"--.",
			"h":"....",
			"i":"..",
			"j":".---",
			"k":"-.-",
			"l":".-..",
			"m":"--",
			"n":"-.",
			"o":"---",
			"p":".--.",
			"q":"--.-",
			"r":".-.",
			"s":"...",
			"t":"-",
			"u":"..-",
			"v":"...-",
			"w":".--",
			"x":"-..-",
			"y":"-.--",
			"z":"--.."
			}

		transformCode=set()
		for word in words :
			tword=''
			for letter in word :
				tword +=morseTable[letter]
			transformCode.add(tword)
		return len(transformCode)

obj=Solution()
print(obj.uniqueMorseRepresentations(["gin","zen","gig"]))
