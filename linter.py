import sys
import re

OPENING_BRACKET_REGEX = re.compile("[\{]")
CLOSING_BRACKET_REGEX = re.compile("[\}]")

class Linter:

	def __init__(self,filePath):
		self.content = []
		self.readFile(filePath)
		self.maxLineLength = 600

	def getScore(self):
		self.testLineLength()
		print self.indentation()

	def readFile(self,filePath):
		with open(filePath) as f:
			self.content = f.readlines()
		# you may also want to remove whitespace characters like `\n` at the end of each line
		#self.content = [x.strip() for x in self.content] 


	def printContent(self):
		for i in range(len(self.content)):
 			print len(self.content[i])


 	def testLineLength(self):
 		for i in range(len(self.content)):
 			if(len(self.content[i]) > self.maxLineLength):
 				print "this line is too long: " + self.content[i]			

 	def indentation(self):
 		curlyNumber = 0
 		numberOfLines = len(self.content)
 		fail = 0
 		success = 0
 		for i in range(len(self.content)):

 			checkCurly = False
 			countSpace = True
 			numberOfSpaces = 0

 			if(OPENING_BRACKET_REGEX.search(self.content[i])):
 				curlyNumber += 1
 				checkCurly = True

 			if(CLOSING_BRACKET_REGEX.search(self.content[i])):
 				curlyNumber -= 1
 				checkCurly = True

 			if(not(re.match("[\t]{" + str(curlyNumber) + "}[^\t\ ]", self.content[i])) and \
 			not(re.match("[\ ]{" + str(curlyNumber*4) + "}[^\t\ ]", self.content[i])) and checkCurly == False):
 				fail += 1

 		return (float(numberOfLines - fail)/numberOfLines)*100.0			

 						

if __name__ == '__main__':
	myLint = Linter(sys.argv[1])
	myLint.getScore()		
