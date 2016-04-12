def getUserInput():
    try:
        userInput= list(input ('Enter numbers to check: '))
        userInput= [int(intigers) for intigers in userInput]
    except:
        print('Not a valid number')
        return (getUserInput())
    return userInput
def convertUserInput():
    intValues = str(getUserInput())
    return (intValues)
def firstOrLastIs6(convertedUserInput):
    if convertedUserInput.startswith('6'):
        return ('true')
    elif convertedUserInput.endswith('6'):
        return ('true')
    else:
        return ('false')
answer = firstOrLastIs6(convertUserInput())
print (answer)
    
