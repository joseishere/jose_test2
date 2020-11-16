
types = {
    'byte':'byte',
    'short':'short',
    'int':'int',
    'long':'long',
    'float':'float',
    'double':'double',
    'boolean':'boolean',
    'char':'char',
}

def startChecker(arr):
    haveWhile = False
    haveIf = False
    # print(arr[:2])
    # print(arr[:5])
    if(arr[:5] == 'while'):
        # print('we have while at the start')
        haveWhile = True
        return True and checkBool(arr[5:])
    elif(arr[:2] == 'if'):
        # print('we have an if')
        haveIf = True
        return True and checkBool(arr[2:])
    else:
        # lets find if we have an =
        equalSign = arr.find('=')
        if(equalSign != -1):
            # need to see if we have variable type and a value and a ;
            return True and checkVar(arr, equalSign)
        else:
            return False
    return False

def checkBool(end):
    parenCount = 0
    curlyCount = 0
    startBool = False
    totalBool = False
    for char in end:
        if(char == '('):
            parenCount += 1
        elif(char == ')'):
            parenCount -= 1
        elif(char == '{'):
            curlyCount += 1
        elif(char == '}'):
            curlyCount -= 1
        elif(char == '>' or char == '<' or char == '='):
            startBool = True
        if(startBool and char == '='):
            totalBool = True
            startBool = False
    return (startBool or totalBool) and (curlyCount == 0) and (parenCount == 0)

def checkVar(arr, equalSign):
    done = False
    #print(arr[equalSign+1: ])
    wordsBefore = arr[:equalSign].split()
    #print(wordsBefore)
    if(wordsBefore[0] in types.values()):
        for char in arr[equalSign+1:]:
            #print(char)
            if(done):
                return False
            if(char == ';'):
                done = True
            elif(char == '='):
                return False
            else:
                pass
    if(done):
        return True
    return False

def main():
    validStrings = ['while(x >= 4){}', 'if(x>3){}', 'int num = 3;']
    nonvalidStrings = ['while(x 4){}', 'if(x>3){', 'car num = 3;']

    for string in validStrings:
        if(startChecker(string)):
            print(string + " is valid")
        else:
            print(string + " is not valid")

    for string in nonvalidStrings:
        if(startChecker(string)):
            print(string + " is valid")
        else:
            print(string + " is not valid")

if __name__ == '__main__':
    main()
