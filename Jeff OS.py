#Variable Storage
def startup():
    username = input("Username: ")
    password = input("Please enter the password: ")
    if password == "AAROON":
        print ("Welcome,",username)
        print ("We are the PZ OS")
        print("Open Approved by Jeff Sharer Official")
        print("This is a CUI interface.")
        print("Any wrong spelling can make an error")
        print("You can play a game, or whatever.")
        print("Type Credits if you want to see our credits")
        choice = input("What do you want to do: ")
        if choice == "play":
            play()
        elif choice == "open_browser":
            browser_open()
        elif choice == "Number Calculator":
            calculator()
        elif choice == "Letter Calculator":
            lettercalc()
        elif choice == "Credits":
            ccredits()
        else:
            print ("Error")
            print ("Invalid Syntax")
            print ("Check your spelling or view the only choices you can do.")
    else:
        print ("Wrong Password")
        print ("PZ OS is very unforgiving!")




def ccredits():
    print ("PZ OS")
    print ("Created with Python 3.7.1")
    print ("Typed in IdlE")
    print ("Made in one day for 3 versions")
    exit





def calculator():
    print ("Welcome to the Jeff OS Calculator")
    num1 = int (input("Enter the first number: "))
    num2 = int (input("Enter the second number: "))
    op = input("What is the operation: ")
    if op == "+":
        print (num1 + num2)
    elif op == "-":
        print (num1 - num2)
    elif op == "*":
        print (num1 * num2)
    elif op == "/":
        print (num1 / num2)
    elif op == "**":
        print (num1 ** num2)
    else:
        print ("Invalid syntax")
        print ("Available operations are:")
        print ("+ - * / **")


def lettercalc():
    user_letter_calc_input = len (input("""Enter the text so we can check how many letters your text has.
Do not use Space if you dont want the space to be counted: """))
    print (user_letter_calc_input)
    
    
    


    




def play():
    games = input("What game do you want to play: ")
    print ("The only games are quiz, mad libs.")

    if games == "quiz":
        quiz()
    elif games == "mad libs":
        madlibs()



def browser_open():
    import webbrowser
    webbrowser. open("www.google.com")


def quiz():
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



def madlibs():
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

    

#story board JOSLS
startup()

