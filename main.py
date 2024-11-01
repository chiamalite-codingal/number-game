import random
computerguess = random.randint(1,8)
print("I am thinking of number betweem 1 and 8")
while True:
    userguess = int(input("Enter your guess:"))
    if userguess == computerguess:
        print("you guessed right!!")
    else:
        print("COMPUTER GUESS IS:",computerguess)
        print("you're wrong!,Try again")