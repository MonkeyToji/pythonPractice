import random
secretNumber = random.randint(1, 20)
print('Im thinking of a number between 1 and 20')

#Ask player to answer 6 times
for guessessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is to low')
    elif guess > secretNumber:
        print('to high')
    else:
        break #Correct guess

if guess == secretNumber:
    print('You got it in ' + str(guessessTaken) + ' guesses!')
else:
    print('Sorry, I was thinking of ' + str(secretNumber))
