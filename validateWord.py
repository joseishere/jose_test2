# validateWord.py
# this file: what will combine all the others and test all of the words
# I didn't really know what question was asking so what I did was just validate if each word
# valid for its respective type
# Now I think that I may have done this question wrong but that is what I took it as
# I wish the question was worded differently
# and I hope that I can get some credit for doing all of this

from getWords import fromFile
from tryChar import charChecker
from tryFloat import floatChecker
from tryInt import intChecker
from tryJava import javaChecker
from tryOperator import operatorChecker
from tryPerl import perlChecker


def callFuncs(arr):
    # this could be done so much better but tired
    result = [0] * 6
    if(charChecker(arr)):
        result[0] = 1
    if(floatChecker(arr)):
        result[1] = 1
    if(intChecker(arr)):
        result[2] = 1
    if(javaChecker(arr)):
        result[3] = 1
    if(operatorChecker(arr)):
        result[4] = 1
    if(perlChecker(arr)):
        result[5] = 1
    return result

def main():
    words = fromFile('testInputs.txt')
    for word in words:
        print()
        print(word)
        index = 0
        for result in callFuncs(word):

            # print(result)
            # if(result):
            #     print(word + ': \t\t\t VALID')
            if(index == 0):
                if(result):
                    print(word + " C Char: \t\t\t VALID")
                else:
                    print(word + " C Char: not VALID")
                index+=1
            elif(index == 1):
                if(result):
                    print(word + " C Float: \t\t\t VALID")
                else:
                    print(word + " C Float: not VALID")
                index+=1
            elif(index == 2):
                if(result):
                    print(word + " C Int: \t\t\t VALID")
                else:
                    print(word + " C Int: not VALID")
                index+=1
            elif(index == 3):
                if(result):
                    print(word + " Java String: \t\t\t VALID")
                else:
                    print(word + " Java String: not VALID")
                index+=1
            elif(index == 4):
                if(result):
                    print(word + " Operator: \t\t\t VALID")
                else:
                    print(word + " Operator: not VALID")
                index+=1
            elif(index == 5):
                if(result):
                    print(word + " Perl Identifier: \t\t\t VALID")
                else:
                    print(word + " Perl Identifier: not VALID")
                index+=1
            else:
                print('Done')




if __name__ == '__main__':
    main()
