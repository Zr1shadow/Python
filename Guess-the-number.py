import random

secretNumber = random.randint(1, 20)
i = 0
while i < 4:
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
        i += 1
    elif guess > secretNumber:
        print('Your guess is too high.')
        i += 1
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(i) + '\
 guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
