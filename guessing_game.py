#In this problem, you'll create a program that guesses a secret number!

#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
#The computer makes guesses, and you give it input - is its guess too high or too low?
#Using bisection search, the computer will guess the user's secret number!

print('Please think of a number between 0 and 100!')
low = 0
high = 100
ans = (high + low)/2
response = ''
print('Is your secret number ' + str(ans) + '?')
while True:
    response = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if response == 'h':
        high = ans
        ans = (high + low)/2
        print('Is your secret number ' + str(ans) + '?')
    elif response ==  'l':
        low = ans
        ans = (high + low)/2
        print('Is your secret number ' + str(ans) + '?')
    elif response == 'c':
        ans = (high + low) /2
        print('Game over. Your secret number was: ' + str(ans))
        break
    else:
        ans = (low+high)/2
        print"Sorry, I did not understand your input."
        print('Is your secret number ' + str(ans) + '?')
