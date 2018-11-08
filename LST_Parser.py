# List Set Tuple Parser
# Written by Guru Sarath
# Date: 21th Oct 2018

# This is the main function that should be used to parse lists, sets and tuples in python (Dictionaries not allowed)
def LST_parse(lineX):
	lineX = identifyType(lineX)

	#If a valid string is given as input
	if lineX != 'Invalid':
		typeX = lineX[:3]
		lineX = lineX[3:]

		structureX = None

		if typeX == 'lis':
			structureX = splitAtCommas(lineX)
		elif typeX == 'set':
			structureX = splitAtCommas(lineX)
		elif typeX == 'tup':
			structureX = splitAtCommas(lineX)
		elif typeX == 'str':
			structureX = lineX[1:-1]
			return structureX
		elif typeX == 'num':
			structureX = lineX
			if '.' in lineX:
				valueOfNum = float(structureX)
			else:
				valueOfNum = int(structureX)
			return valueOfNum

		if typeX == 'lis' or typeX == 'set' or typeX == 'tup':
			for i in range(len(structureX)):
				#Recursive call
				parseNext = LST_parse(structureX[i])
				if parseNext != 'Invalid':
					structureX[i] = parseNext
				else:
					return 'Invalid'

			#Convert the list to a tuple if it is of type tuple
			if typeX == 'tup':
				structureX = tuple(structureX)

			#convert the list to a set if it is of type set
			if typeX == 'set':
				structureX = set(structureX)

			#RETURN the final processed structure
			return structureX
	else:
		#invalid type (syntax issue in the string)
		return 'Invalid'

# find type of the input (list or tuple or set or number or string)
# This function appends three letters at the start of the string to mention the typea
def identifyType(lineX):

	#Check if an empty string is passed
	if lineX != '':
		# List starts with [ and ends with ]
		if lineX[0] == '[' and lineX[-1] == ']':
			return 'lis' + lineX
		# Set starts with { and ends with }
		elif lineX[0] == '{' and lineX[-1] == '}':
			return 'set' + lineX
		# Tuple starts with ( and ends with )
		elif lineX[0] == '(' and lineX[-1] == ')':
			return 'tup' + lineX
		# strings starts with ' and ends with '
		elif (lineX[0] == '\'' and lineX[-1] == '\'') or (lineX[0] == '\"' and lineX[-1] == '\"'):
			return 'str' + lineX
		#Numbers and decimal point
		elif lineX[0] in '1234567890.':
			return 'num' + lineX

		else:
			#Invalid type (syntax issue in the string)
			return 'Invalid'
	else:
		#Empty string
		return 'Invalid'

# This function gets the individual elements of the list in form of string
def splitAtCommas(inputString, splitMark = '~'):
	bracketCount = 0
	string_started_flag = False #This flag is used to monitor start and end of strings
	outputString = inputString

	for i in range(len(inputString)):
		if (inputString[i] == '[' or inputString[i] == '{' or inputString[i] == '(' or inputString[i] == '\'') and string_started_flag == False:
			bracketCount += 1
			if inputString[i] == '\'':
				string_started_flag = True
		elif inputString[i] == ']' or inputString[i] == '}' or inputString[i] == ')' or (inputString[i] == '\'' and string_started_flag == True):
			if string_started_flag == False:
				bracketCount -= 1
			if inputString[i] == '\'':
				bracketCount -= 1
				string_started_flag = False
		elif inputString[i] == ',' and bracketCount == 1:
			outputString = outputString[:i] + splitMark + outputString[i+1:]

	outputString = outputString[1:-1]
	outputString =  outputString.split(splitMark) #split all the elements in the list

	trimmed_output_list = list();

	for x in outputString:
		#remove any leading and trailing spaces in the input string and append
		trimmed_output_list.append(x.strip())

	return trimmed_output_list