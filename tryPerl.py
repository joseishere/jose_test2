# tryPerl.py
def perlChecker(word):
    if(len(word) < 2):
        return False
    foundStart = None
    for letter in word:
        if(letter.isalnum() or letter == '$' or letter == '@' or letter == '%' or letter == '_'):
            if (foundStart == None):
                if( (letter == "$" or letter == "%" or letter == "@")):
                    foundStart = letter
                else:
                    return False
            else:
                # now we just need numbers or underscore
                if( letter.isalnum() or letter == "_"):
                    pass
                else:
                    return False
        else:
            return False
    return True

def main():

    words = ['$var_sas', '@another2', '@test', '%another\s', '$test_$', '#testt', '@test#w']
    for word in words:
        if(perlChecker(word)):
            print(word + " is valid")
        else:
            print(word + " is not valid")


if __name__ == "__main__":
    main()
