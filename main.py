
# Ruby Solis-Chavez, Anabel Perez

# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
from jokes2 import finished, robbers, tanks, pencils


def get_joke(): # Function gets the type of joke that the user wants to hear
    joke_types = [robbers, tanks, "pencils" ] #list of jokes available

    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ") # Allows user to input if they want to hear a robber, tank, or pencil joke
    if question == "robbers":
            robbers() # Will run if user wanted to hear a joke about robbers
    
    elif question == "tanks":
            tanks() #will run the dialouge for tanks joke

    elif question == "pencils":
        pencils() #will run the dialouge for pencils joke


def want_jokes(): # Function asks user if they want to hear a joke
    joke = input("Do you want to hear a joke? ")
    if joke == "no": # If user didn't want to hear the joke, this will print and the code will end
        print("Okay suit yourself!") 
    elif joke == "yes":# If user wanted to hear joke, will run the get_joke() function defined above
        print("Great, Let's Play")
        get_joke()




def multi_jokes(**jokes): #function runs the whole game
    

    want_jokes() 
    if jokes == "yes": # If statement runs different functions based off of user's answer of yes or no
        get_joke()
    elif jokes == "finished":
        finished() 
        
    
    
multi_jokes() # calls function to run

    #     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    #     if question == "robbers":
    #         input("Knock Knock ")
    #         input("Calder")
    #         print("Calder police - I've been robbed!")
    #         joke = input("Do you want to hear another joke or are you finished? ")
    #     elif question == "tanks":
    #         input("Knock Knock ")
    #         input("Tank ")
    #         input("You are welcome! ")
    #         joke = input("Do you want to hear another joke or are you finished? ")
    #     elif question == "pencils":
    #         input("Knock Knock ")
    #         input("Broken pencil ")
    #         input("Nevermind, it's pointless! ")
    #         joke = input("Do you want to hear another joke or are you finished? ")

    # if joke == "finished":
    #     rate = int(input("Please rate our game 1-10! "))
    #     final_score = int(rate * 10)
    #     print(str(final_score) + " percent satisfaction rate")
    #     friend = input("Would you recommend this game to a friend? ")

    #     if friend == "yes" or friend == "maybe":
    #         print("Thanks, we appreciate it. ")
    #     else:
    #         print("Sorry you did not enjoy it. ")


        # needs lists & parameters( taking diff paths)


