#defined variables


def start():
    print ("Welcome to the Guessing Game")
    print ("You have to guess the word we store")
    ready = input("Ready? ")
    if ready == "yes":
        gamepiece()
    elif ready == "no":
        print ("ok")
        start()



def gamepiece():
    wordinput = input("What do you think is the word: ")
    if wordinput == "zorgo diffuse":
        print ("Correct")
        start()
    else:
        print ("Wrong word")
        print ("Note: The word is case sensitive")
        start()




#main storyboard
start()



