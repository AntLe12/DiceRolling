import random


def randomlyChooseNumber():
    print(random.randint(1, 6))


print("Would you like to roll a dice? Please enter Yes or No?")  # Asks for user to say yes or no
userReply = input()
if userReply == "Yes" or userReply == "yes": # Checks for if the user said yes
    randomlyChooseNumber()
else:
    print("You're no fun!")
    stop = "No"

stop = userReply
while stop != "No": # Runs as long as the user hasn't said no
    print("Do you still want to roll a dice? Please enter Yes or No?")
    userReply = input()
    if userReply == "Yes" or userReply == "yes":  # Checks for if the user said yes
        randomlyChooseNumber()
    else:
        stop = "No"
print("You're no fun!")