import random

a = str(random.randint(1, 10))
def guess():
    global a
    b = input("Guess the number between 1 and 10: ")
    if b == a:
        print("You guessed it right!")
        pass
    else:
        print("Wrong guess!")
        guess()
        

guess()