print ("Welcome to the Quizzzzzz Game")
print ("Created with Python 3")
print ("Hope you like it")
print ("To play just fill in the blanks")

MC = input ("Who Created Microsoft: ")
Apple = input ("What does Apple use to create apps: ")
Facebook = input ("Mark Zukenberg Created: ")

print ("This is how the blanks look like.")
print (MC,"created Microsoft")
print ("Apple uses", Apple, "to create apps")
print ("Mark Zukenberg created", Facebook)

print ("Answers are: ")
print ("No.1 is Bill Gates")
print ("No.2 is xCode")
print ("No.3 is Facebook")

right = input ("How many questions did you get right? ")
ans = int (right) / 3 * 100
print ("Your score is", int (ans))
