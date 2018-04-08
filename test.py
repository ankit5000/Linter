import sys

# with open("3.pl") as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content] 

# print len(content[0])

# # for i in range(len(content)):
# # 	print len(content[i])
# print content[2][10]

class Linter:

	def __init__(self,filePath):
		self.content = []
		self.readFile(filePath)
		self.maxLineLength = 60

	def getScore(self):
		self.testLineLength()	

	def readFile(self,filePath):
		with open(filePath) as f:
			self.content = f.readlines()
		# you may also want to remove whitespace characters like `\n` at the end of each line
		self.content = [x.strip() for x in self.content] 


	def printContent(self):
		for i in range(len(self.content)):
 			print len(self.content[i])


 	def testLineLength(self):
 		for i in range(len(self.content)):
 			if(len(self.content[i]) > self.maxLineLength):
 				print "this line is too long: " + self.content[i]

 				


if __name__ == '__main__':
	myLint =  Linter(sys.argv[1])
	myLint.getScore()		


