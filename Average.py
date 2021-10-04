average = 0
total = 0
howManyEntered = 0
print('How many test scores would you like to average?')
howMany = int(input(''))
while howManyEntered < howMany:
    print('Enter test score:')
    testScore = int(input(''))
    total = total + testScore
    howManyEntered = howManyEntered + 1
    print("Total is: ", total)
    print('How many entered is: ', howManyEntered)
average = total/howMany
print('The average for the test scores you entered is: ', average)
