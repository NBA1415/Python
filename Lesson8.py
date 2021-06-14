#I/O
Name = input("Please enter your name: ") #str
print(Name)

#Age = input("Please enter your age: ")
#can't print (Age + 1)
Age = int(input("Please enter your age: "))
print (Age + 1)
#compare
print (str(Age)+"1")
# alternative - see the difference
Age = input("Please enter your age: ")
print (int(Age)+1)
#to use as str
Scores = []
for i in range(5):
	currentScore = int(input("Please enter the score: "))
	Scores.append(currentScore)
print (Scores)
Scores = []
for i in range(5):
	currentScore = int(input("Please enter the score "+str(i+1) +": "))
	Scores.append(currentScore)
print (Scores)
Scores = []
for i in range(5):
	currentScore = float(input("Please enter the score "+str(i+1) +": "))
	Scores.append(currentScore)
	print("The score you entered was:",currentScore,"nice") #note , vs +
# comma adds a space
# looks like
#def FunctionName(input1, input2, input3)
# Action
print (Scores)
Scores = []
for i in range(5):
	currentScore = float(input("Please enter the score "+str(i+1) +": "))
	Scores.append(currentScore)
	print("The score you entered was:\n"+str(currentScore)) #\n add new line
# comma adds a space
# looks like
#def FunctionName(input1, input2, input3)
# Action
print (Scores)
