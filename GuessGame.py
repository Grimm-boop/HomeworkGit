import random

difficulty = 5
secret_number = 0

def generate_number():
    global secret_number
    secret_number = random.randint(0, difficulty)
def get_guess_from_user():
    return input( "Please choose number between 1 to " + str(difficulty))
def compare_results(userInput):
    isSame = False

    if(secret_number == userInput):
        isSame = True

    return isSame
def play():
    generate_number()
    userInput = get_guess_from_user()
    isSame = compare_results(userInput)
    print("number generated is: " + str(secret_number))
    print(isSame)

play()