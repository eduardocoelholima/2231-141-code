# when does the house wins?
# when the player wins?
# when is the number chosen not allowed?

def silly_game():
    number = input("Choose a number: ")

    if int(number) < 0:
        print("You can not choose a negative number!")
    elif int(number) < 5:
        print("The house wins!")
    else:
        print("Alright, you won this one")

silly_game()