
# Ruby Solis-Chavez, Anabel Perez

# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

joke = input("Do you want to hear a joke? ")
if joke == "no":
    print("Okay suit yourself!")
while joke == "yes":
    print("Great, Let's Play")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    if question == "robbers":
            robbers() # Will run if user wanted to hear a joke about robbers
    
    elif question == "tanks":
            tanks() #will run the dialouge for tanks joke

    elif question == "pencils":
        input("Knock Knock ")
        input("Broken pencil ")
        input("Nevermind, it's pointless! ")
        joke = input("Do you want to hear another joke or are you finished? ")
if joke == "finished":
    rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")
