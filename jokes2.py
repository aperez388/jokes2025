def finished():
    rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")
    return
    


def robbers():
    robbers_list = ["Knock Knock ", "Calder ", "Calder police - I've been robbed! "]
    input(robbers_list[0])
    input(robbers_list[1])
    print(robbers_list[2])
    joke = input("Do you want to hear another joke or are you finished? ")
    if joke == "finished":
        finished()
    


def tanks():
    tanks_list = ["Knock Knock ", "Tank ", "You are welcome! "]
    input(tanks_list[0])
    input(tanks_list[1])
    print(tanks_list[2])
    joke = input("Do you want to hear another joke or are you finished? ")
    if joke == "finished":
        finished()

def pencils():
    pencils_list = ["Knock Knock ", "Broken pencil ", "Nevermind, it's pointless! "]
    input(pencils_list[0])
    input(pencils_list[1])
    print(pencils_list[2])
    joke = input("Do you want to hear another joke or are you finished? ")
    if joke == "finished":
        finished()
