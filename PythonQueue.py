names = []
while len(names)<10:
    print('Input 10 names')
    acceptedName = str(input(''))
    names.append(acceptedName)
print(names)
while len(names)>0:
    print(names.pop(0))
print('Queue is empty')
