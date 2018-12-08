#Hello() Defined
def hello():
    print ("HELLO")
    print ("Welcome to the Mad Libs Game")

#Game Piece Defined

def gamepiece():
    hello()
    story()

#Story Defined

def story():
    print ("My name is [name], I like to [verb], [verb] makes me [feelings].")
    print ("At the age of [age], I like to [verb2].")
    print ("This is my favorite poem")
    print ("[Flower1] are red")
    print ("[Flower2] are blue")
    print ("I [like/hate/love] you")



#Storyboard

gamepiece()

name = input("Name: ")
verb = input("Verb: ")
feelings = input("Feelings: ")
Flower1 = input("Flower1: ")
Flower2 = input("Flower2: ")
expression = input("What is the expression [Choose love/hate/like]: ")
age = input("Age of when you like the hobby: ")

print ("Here are your results: ")
print ("My name is " + name + ", I like to " + verb + ",", verb, "makes me",feelings,".")
print ("At the age of " + age + ", I like to [verb2].")
print ("This is my favorite poem")
print (Flower1, "are red")
print (Flower2, "are blue")
print ("I "+expression+" you")


likehategame = input("Did you like this game: ")
if likehategame == "Yes":
    print ("Thanks, hope you try with your friends.")
elif likehategame == "No":
    print ("I am sorry that you don't like it. We are going to improve this next time.")
