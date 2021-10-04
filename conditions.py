temp = 0
print('Please enter the current temperature in Fahrenheit or 999 to end:')
while temp != 999:
    temp = int(input(''))
    if temp == 999:
        print('Program has ended')
        break
    elif temp > 90:
            print('Wear shorts')
    elif temp > 70:
            print('Short sleeves are fine')
    elif temp > 50:
            print('Wear a jacket')
    elif temp > 32:
            print('Wear a heavy coat')
    else:
            print('Stay inside')
