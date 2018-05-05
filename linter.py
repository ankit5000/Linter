import sys
import re

OPENING_BRACKET_REGEX = re.compile("[\{]")
CLOSING_BRACKET_REGEX = re.compile("[\}]")

COMMENT_1_REGEX = re.compile(r'\/{2}')
COMMENT_2_OPEN_REGEX = re.compile(r'\/\*')
COMMENT_2_CLOSE_REGEX = re.compile(r'\*\/')

BLANK_LINE_REGEX = re.compile("\n")

FUNCTION_REGEX = re.compile("(?![a-z])[^\:,>,\.]([a-z,A-Z]+[_]*[a-z,A-Z]*)+[(]")

class Linter:

	def __init__(self,filePath, reportPath):
		self.content = []
		self.readFile(filePath)
		self.totalLines = len(self.content)
		self.maxLineLength = 80
		self.score = 0
		self.file_writer = open(reportPath, "w")

	def readFile(self,filePath):
		with open(filePath) as f:
			self.content = f.readlines()


	def printContent(self):
		for i in range(self.totalLines):
 			print len(self.content[i])


 	def testLineLength(self):
 		longLines = 0
		self.file_writer.write('LONG LINES REPORT: \n')
 		for i in range(self.totalLines):
 			if(len(self.content[i]) > self.maxLineLength):
 				longLines += 1
				self.file_writer.write('Line %d: %s'%(i+1, self.content[i]))
		if (longLines==0):
			self.file_writer.write('No long lines\n')
 		print "Number Of Long Lines: " + str(longLines) + " (" + '%.2f' % (10*(1 - float(longLines)/self.totalLines)) + "/10.00)"
 		return longLines


 	def indentation(self):
		self.file_writer.write('\nINDENTATION REPORT:\n')
 		curlyNumber = 0
 		fail = 0
 		success = 0
 		for i in range(self.totalLines):

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
 			not(re.match("[\ ]{" + str(curlyNumber*4) + "}[^\t\ ]", self.content[i])) and checkCurly == False and self.content[i]!="\n"):
 				fail += 1
				self.file_writer.write('Bad indentation in Line %d\n'%(i+1))
		if (fail==0):
			self.file_writer.write('All lines properly indented\n')
 		indScore = 100*(1 - float(fail)/self.totalLines)

 		if(indScore > 90):
 			print "Indentation: Good " + "(" + '%.2f' % (indScore/2.0) + "/50.00" + ")"

 		elif(indScore > 60):
 			print "Indentation: Average " + "(" + '%.2f' % (indScore/2.0) + "/50.00" + ")"

 		else:
 			print "Indentation: Poor " + "(" + '%.2f' % (indScore/2.0) + "/50.00" + ")"

 		return fail


 	def comment(self):
		numberOfComments = 0
		check = False
		self.file_writer.write('\nCOMMENTS REPORT\n')
		for i in range(self.totalLines):
			if(COMMENT_1_REGEX.search(self.content[i])):
				numberOfComments += 1
		temp = 0;
		for i in range(self.totalLines):
			if(COMMENT_2_OPEN_REGEX.search(self.content[i])):
				temp = 1
				check = True
			elif(COMMENT_2_CLOSE_REGEX.search(self.content[i]) and check):
				temp += 1
				check = False
				numberOfComments += temp
				temp = 0
			elif(check):
				temp += 1

		commScore = 100*(float(numberOfComments*3)/self.totalLines)

		self.file_writer.write('No of comments in the code: %d\n'%(numberOfComments))
		self.file_writer.write('No of comments ideal for your code: %d\n'%(self.totalLines/3))

		if(commScore >= 20):
			print "Number of comments: Appropriate" + " (" + '%.2f' % min(20, 20*(float(numberOfComments*3)/self.totalLines)) + "/20.00" + ")"

		else:
			print "Number of comments: Not Sufficient" + " (" + '%.2f' % min(20, 20*(float(numberOfComments*3)/self.totalLines)) + "/20.00" + ")"

		return numberOfComments


	def blankLine(self):
		self.file_writer.write('\nBLANK LINE REPORT\n')
		numberOfBlankLines = 0
		for i in range(self.totalLines):
			if(BLANK_LINE_REGEX.match(self.content[i])):
				numberOfBlankLines += 1

		blankScore = 100*(float(numberOfBlankLines)/self.totalLines)
		self.file_writer.write('No of blank lines in the code: %d\n'%(numberOfBlankLines))

		if(blankScore > 60):
			print "Blank Lines: Too Many " + "(7.00/10.00)"

		elif(blankScore > 10):
			print "Blank Lines: Appropriate " + "(10.00/10.00)"

		else:
			print "Blank Lines: Very Few " + "(7.00/10.00)"

		return numberOfBlankLines


	def functionAvail(self):
		self.file_writer.write('\nFUNCTION LENGTH REPORT\n')
		cnt = []
		func_name = ''
		check = False
		temp = 0
		brack = 0
		error = 0
		total = 0
		for strng in self.content:
			if(FUNCTION_REGEX.search(strng)):
				temp = 1
				error = 0
				brack = 0
				check = True
				func_name = strng
			if(check and OPENING_BRACKET_REGEX.search(strng)):
				brack += 1
			elif(check and CLOSING_BRACKET_REGEX.search(strng)):
				brack -= 1
			if(check and brack == 0 and error != 0):
				total += 1
				if temp > 20:
					cnt.append(temp)
					self.file_writer.write('Long function : %s\n'%(func_name))
				temp = 0
				check = False
			temp += 1
			error += 1
		if len(cnt)==0:
			self.file_writer.write('No long functions\n')

		print "Number of long functions:" + str(len(cnt)) + " (" + '%.2f' % (10*(1 - float(len(cnt))/self.totalLines)) + "/10.00" + ")"

		return len(cnt),total



	def getScore(self):

		p1 = self.testLineLength()
		p2 = self.indentation()
		p3 = self.comment()
		p4 = self.blankLine()
		p5,numberOfFunctions = self.functionAvail()

		self.score += 10*(1 - float(p1)/self.totalLines) + 50*(1 - float(p2)/self.totalLines) + min(20, 20*(float(p3*3)/self.totalLines)) + \
		 10*(1 - float(p5)/numberOfFunctions)

		if(100*(float(p4)/self.totalLines) < 60 and 100*(float(p4)/self.totalLines) > 10):
			self.score += 10.0
		else:
			self.score += 7.0

		print "Code Beauty Metric: " + '%.2f' % self.score + "%"


if __name__ == '__main__':
	myLint = Linter(sys.argv[1], sys.argv[2])
	myLint.getScore()
